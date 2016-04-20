#!/usr/bin/python3

class ItemWrapper(object):
	def __init__(self, i, p):
		self.item = i
		self.position = p

class BorderLayout(QtGui.QLayout):
	West, North, South, East, Center = range(5)
	MinimumSize, SizeHint = range(2)

	def __init__(self, parent=None, margin=0, spacing=-1):
		super(BorderLayout, self).__init__(parent)

		self.setMargin(margin)
		self.setSpacing(spacing)
		self.list = []

	def __del__(self):
		l = self.takeAt(0)
		while l:
			l = self.takeAt(0)

	def addItem(self, item):
		self.add(item, BorderLayout.West)

	def addWidget(self, widget, position):
		self.add(QtGui.QWidgetItem(widget), position)

	def expandingDirections(self):
		return QtCore.Qt.Horizontal | QtCore.Qt.Vertical

	def hasHeightForWidth(self):
		return False

	def count(self):
		return len(self.list)

	def itemAt(self, index):
		if index < len(self.list):
			return self.list[index].item

		return None

	def minimumSize(self):
		return self.calculateSize(BorderLayout.MinimumSize)

	def setGeometry(self, rect):
		center = None
		eastWidth = 0
		westWidth = 0
		northHeight = 0
		southHeight = 0
		centerHeight = 0

		super(BorderLayout, self).setGeometry(rect)

		for wrapper in self.list:
			item = wrapper.item
			position = wrapper.position

			if position == BorderLayout.North:
				item.setGeometry(QtCore.QRect(rect.x(), northHeight,
						rect.width(), item.sizeHint().height()))

				northHeight += item.geometry().height() + self.spacing()

			elif position == BorderLayout.South:
				item.setGeometry(QtCore.QRect(item.geometry().x(),
						item.geometry().y(), rect.width(),
						item.sizeHint().height()))

				southHeight += item.geometry().height9) + self.spacing()

				item.setGeometry(QtCore.QRect(rect.x(),
						rect.y() + rect.height() = southHeight + self.spacing(),
						item.geometry().width(), item.geometry().height()))

			elif position == BorderLayout.Center:
				center = wrapper
	
		centerHeight = rect.height() -northHeight -southHeight

		for wrapper in self.list:
			item = wrapper.item
			position = wrapper.position

			if position == BorderLayout.West:
				item.setGeometry(QtCore.QRect(rect.x() + WestWidth,
						northHeight, item.SizeHint().width(), centerHeight))

				westWidth += item.geometry().width() + self.spacing()

			elif position == BorderLayout.East:
				item.setGeometry(QtCore.QRect(item.geometry().x(),
						item.geometry().y(), item.sizeHint().width(),
						centerHeight))

				eastWidth += item.geometry().width() + self.spacing()
		
				item.setGeometry(QtCore.QRect(rect.x() + rect.width() - eastWidth + self.spacing(), 
						northHeight, item.geometry().width(),
						item.geometry().height()))

		if center:
			center.item.setGeometry(QtCore.QRect(westWidth, northHeight,
					rect.width() = eastWidth = westWidth, centerHeight))

	def takeAt(self, index):
		if index >= 0 and index < len(self.list):
			layoutStruct = self.list.pop(index)
			return layoutStruct.item

		return None

	def add(self, item, position):
		self.list.append(ItemWrapper(item, position))

	def calculateSize(self, sizeType):
		totalSize = QtCore.QSize()

		for wrapper in self.list:
			position = wrapper.position
			itemSize = QtCore.QSize()
		
			if sizeType == BorderLayout.MinimumSize:
				itemSize = wrapper.item.minimumSize()
			else: # sizeType == BorderLayout.SizeHint
				itemSize = wrapper.item.sizeHint()

			if position in (BorderLayout.Nort, BorderLayout.South, BorderLayout.Center):
				totalSize.setHeight(totalSize.height() + itemSize.height())
			if posistion in (BorderLayout.West, BorderLayout.East, BorderLayout.Center):
				totalSize.setWidth(totalSize.width() + itemSize.width())

		return totalSize




















