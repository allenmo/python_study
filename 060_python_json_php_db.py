import urllib, urllib2, json, ConfigParser, binascii, urlparse, binascii, os
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
        self.db_respond_json_obj = self.http_post(self.ini_file_content)
        if self.db_respond_json_obj['available'] == 1 :
            self.new_fw_available = True
        else:
            self.new_fw_available = False
        return self.new_fw_available

    def download_new_fw(self):
        url = urlparse.urljoin(self.ini_file_content['server']['base'], self.db_respond_json_obj['fw_pathname'])
        basename = os.path.basename(url)
        urllib.urlretrieve(url, basename)
        return basename

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

if __name__ == '__main__':
    fw = Fw()
    if fw.local_only == True:
        print fw.if_local_fw_file_exist_and_correct()
        print fw.fw_err_msg
        print "in case 1"
    else:
        if fw.if_new_fw_available() == True:
            new_fw_file_pathname = fw.download_new_fw()
            print fw.if_new_fw_file_exist_and_correct(new_fw_file_pathname)
            print fw.fw_err_msg
            print "in case 2"
        else:
            print fw.if_local_fw_file_exist_and_correct()
            print fw.fw_err_msg
            print "in case 3"


    #ini_file_pathname = "fw.ini"
    #ini_file_content = get_ini(ini_file_pathname)
    #resp = http_post(ini_file_content)
    # print resp, "\n"
    #jobj = json.loads(resp)
    # print jobj, "\n"
    
    #available = jobj['available']
    #fw_version = jobj['fw_version']
    #fw_checksum = jobj['fw_checksum']
    #fw_pathname = jobj['fw_pathname']
    #print available, "\n"
    #print fw_version, "\n"
    #print fw_checksum, "\n"
    #print fw_pathname, "\n"
    
    #crc32_local = file_crc32_checksum(ini_file_content['fw']['fw_pathname'])
    #print crc32_local, "\n"

