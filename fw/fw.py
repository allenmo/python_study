import urllib, urllib2, json, ConfigParser, binascii, urlparse, binascii, os, time, shutil
class Fw(object):
    def __init__(self, ini_file_pathname='fw.ini'):
        self.ini_file_pathname = ini_file_pathname
        self.ini_file_content = ""
        self.local_only = 0
        self.db_respond_json_obj = ""
        self.new_fw_available = False
        self.ini_file_content = self.get_ini(self.ini_file_pathname)
        self.local_only = self.to_bool(self.ini_file_content['control']['local_only'])
        self.fw_ok = False
        self.fw_err_msg = ""
        self.archive_folder = 'fw_archive'
        self.temp_download_folder = '.temp_fw'
        self.check_and_create_support_folder()

    def check_and_create_support_folder(self):
        if not os.path.exists(self.archive_folder):
            os.makedirs(self.archive_folder)
        if not os.path.exists(self.temp_download_folder):
            os.makedirs(self.temp_download_folder)

    def to_bool(self, str):
        return (str.lower() in ['1', 'yes','true', 'y', 't'])

    def get_ini(self, ini_pathname):
        cf = ConfigParser.ConfigParser()
        cf.read(ini_pathname)
        control = {}
        control['local_only'] = cf.get("control", "local_only")
        fw = {} 
        fw['customer'] = cf.get("fw", "customer")
        fw['model'] = cf.get("fw", "model")
        fw['component_designator'] = cf.get("fw", "component_designator")
        fw['fw_version'] = cf.get("fw", "fw_version")
        fw['fw_pathname'] = cf.get("fw", "fw_pathname")
        fw['fw_checksum'] = cf.get("fw", "fw_checksum").upper()
        server = {}
        server['base'] = cf.get("server", "base")
        server['page'] = cf.get("server", "page")
        ini_file_content = {'control':control, 'fw':fw, 'server':server}
        return ini_file_content
    
    def http_post(self,content):
        url = urlparse.urljoin(content['server']['base'], content['server']['page'])
        values = {'customer': content['fw']['customer'], 
                'model': content['fw']['model'], 
                'component_designator': content['fw']['component_designator'], 
                'fw_version': content['fw']['fw_version'], 
                'fw_checksum':content['fw']['fw_checksum'].upper()}
        jdata = json.dumps(values,sort_keys=True, indent=4)
        req = urllib2.Request(url, jdata)
        response = urllib2.urlopen(req)
        json_str = response.read()
        json_obj = json.loads(json_str)
        return json_obj

    def if_new_fw_available(self):
        # print self.ini_file_content
        self.db_respond_json_obj = self.http_post(self.ini_file_content)
        # print self.db_respond_json_obj
        if self.db_respond_json_obj['available'] == 1 :
            self.new_fw_available = True
        else:
            self.new_fw_available = False
        return self.new_fw_available

    def download_new_fw(self):
        url = urlparse.urljoin(self.ini_file_content['server']['base'], self.db_respond_json_obj['fw_pathname'])
        basename = os.path.basename(url)
        download_pathname = os.path.join(self.temp_download_folder, basename)
        urllib.urlretrieve(url, download_pathname)
        return download_pathname

    def file_crc32_checksum(self, file_pathname):
        with open(file_pathname, 'rb') as f:
            s = hex(int(binascii.crc32(f.read()) & 0xFFFFFFFF)).upper()
        return s

    def if_local_fw_file_exist_and_correct(self):
        if os.path.isfile(self.ini_file_content['fw']['fw_pathname']):
            s = self.file_crc32_checksum(self.ini_file_content['fw']['fw_pathname'])
            if s == self.ini_file_content['fw']['fw_checksum']:
                self.fw_ok = True
                self.fw_err_msg = ""
            else: 
                self.fw_ok = False
                self.fw_err_msg = "local fw file crc32 checksum error"
        else:
            self.fw_ok = False
            self.fw_err_msg = "local fw file not exist"
        return self.fw_ok

    def if_new_fw_file_exist_and_correct(self, fw_pathname):
        if os.path.isfile(fw_pathname):
            s = self.file_crc32_checksum(fw_pathname)
            if s == self.db_respond_json_obj['fw_checksum']:
                fw.fw_ok = True
                fw.fw_err_msg = ""
            else:
                fw.fw_ok = False
                fw.fw_err_msg = "new fw file crc32 checksum error"
        else:
            fw.fw_ok = False
            fw.fw_err_msg = "new fw file not exist"
        return self.fw_ok

    def getDateTimeStr(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

    def mv_fw_to_sw_root(self, temp_pathname):
        basename = os.path.basename(temp_pathname)
        if os.path.isfile(basename):
            basename_splitext = os.path.splitext(basename)
            name = basename_splitext[0]
            ext = basename_splitext[1]
            new_basename = name + "(before " + self.getDateTimeStr() + ")" + ext
            new_archive_pathname = os.path.join(self.archive_folder, new_basename)
            shutil.move(basename, new_archive_pathname)
        shutil.move(temp_pathname, basename)

    def write_fw_info_to_ini(self, ini_pathname):
        cf = ConfigParser.ConfigParser()
        cf.read(ini_pathname)
        # print os.path.basename(self.db_respond_json_obj['fw_pathname'])
        cf.set("fw", "fw_pathname",os.path.basename(self.db_respond_json_obj['fw_pathname']))
        cf.set("fw", "fw_version",self.db_respond_json_obj['fw_version'])
        cf.set("fw", "fw_checksum",self.db_respond_json_obj['fw_checksum'].upper())
        cf.write(open(ini_pathname, "w"))

    def if_ok_for_download(self):
        if self.local_only == True:
            fw_ok = self.if_local_fw_file_exist_and_correct()
            # print self.fw_err_msg
            # print "in case 1"
        else:
            if self.if_new_fw_available() == True:
                new_fw_file_pathname = self.download_new_fw()
                if self.if_new_fw_file_exist_and_correct(new_fw_file_pathname) == True:
                    self.write_fw_info_to_ini(self.ini_file_pathname)
                    self.mv_fw_to_sw_root(new_fw_file_pathname)
                    # print self.fw_err_msg
                    # print "in case 2"
                    fw_ok = True
                else:
                    fw_ok = False
            else:
                fw_ok = self.if_local_fw_file_exist_and_correct()
                # print self.fw_err_msg
                # print "in case 3"
        return fw_ok

if __name__ == '__main__':
    fw = Fw()
    print fw.if_ok_for_download()

