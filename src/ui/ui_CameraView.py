# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CameraView.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from src.config.FrameLabel import FrameLabel
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraView(object):
    def setupUi(self, CameraView):
        CameraView.setObjectName("CameraView")
        CameraView.resize(900, 705)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            CameraView.sizePolicy().hasHeightForWidth())
        CameraView.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(CameraView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameLabel = FrameLabel(CameraView)
        self.frameLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frameLabel.sizePolicy().hasHeightForWidth())
        self.frameLabel.setSizePolicy(sizePolicy)
        self.frameLabel.setMouseTracking(True)
        self.frameLabel.setAutoFillBackground(True)
        self.frameLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.frameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.frameLabel.setObjectName("frameLabel")
        self.verticalLayout.addWidget(self.frameLabel)
        self.line = QtWidgets.QFrame(CameraView)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_8 = QtWidgets.QLabel(CameraView)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(CameraView)
        self.startButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 3, 3, 1, 1)
        self.pauseButton = QtWidgets.QPushButton(CameraView)
        self.pauseButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        self.pauseButton.setObjectName("pauseButton")
        self.gridLayout.addWidget(self.pauseButton, 4, 3, 1, 1)
        self.nFramesCapturedLabel = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nFramesCapturedLabel.sizePolicy().hasHeightForWidth())
        self.nFramesCapturedLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.nFramesCapturedLabel.setFont(font)
        self.nFramesCapturedLabel.setText("")
        self.nFramesCapturedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nFramesCapturedLabel.setObjectName("nFramesCapturedLabel")
        self.gridLayout.addWidget(self.nFramesCapturedLabel, 3, 2, 1, 1)
        self.roiLabel = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.roiLabel.sizePolicy().hasHeightForWidth())
        self.roiLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.roiLabel.setFont(font)
        self.roiLabel.setText("")
        self.roiLabel.setObjectName("roiLabel")
        self.gridLayout.addWidget(self.roiLabel, 5, 1, 1, 1)
        self.imageBufferBar = QtWidgets.QProgressBar(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.imageBufferBar.sizePolicy().hasHeightForWidth())
        self.imageBufferBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.imageBufferBar.setFont(font)
        self.imageBufferBar.setProperty("value", 0)
        self.imageBufferBar.setObjectName("imageBufferBar")
        self.gridLayout.addWidget(self.imageBufferBar, 7, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.imageBufferLabel = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.imageBufferLabel.sizePolicy().hasHeightForWidth())
        self.imageBufferLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.imageBufferLabel.setFont(font)
        self.imageBufferLabel.setText("")
        self.imageBufferLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageBufferLabel.setObjectName("imageBufferLabel")
        self.gridLayout.addWidget(self.imageBufferLabel, 7, 2, 1, 1)
        self.mouseCursorPosLabel = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mouseCursorPosLabel.sizePolicy().hasHeightForWidth())
        self.mouseCursorPosLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.mouseCursorPosLabel.setFont(font)
        self.mouseCursorPosLabel.setText("")
        self.mouseCursorPosLabel.setObjectName("mouseCursorPosLabel")
        self.gridLayout.addWidget(self.mouseCursorPosLabel, 6, 1, 1, 1)
        self.captureRateLabel = QtWidgets.QLabel(CameraView)
        self.captureRateLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.captureRateLabel.sizePolicy().hasHeightForWidth())
        self.captureRateLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.captureRateLabel.setFont(font)
        self.captureRateLabel.setText("")
        self.captureRateLabel.setObjectName("captureRateLabel")
        self.gridLayout.addWidget(self.captureRateLabel, 3, 1, 1, 1)
        self.processingRateLabel = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.processingRateLabel.sizePolicy().hasHeightForWidth())
        self.processingRateLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.processingRateLabel.setFont(font)
        self.processingRateLabel.setText("")
        self.processingRateLabel.setObjectName("processingRateLabel")
        self.gridLayout.addWidget(self.processingRateLabel, 4, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 7, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.deviceUrlLabel = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.deviceUrlLabel.sizePolicy().hasHeightForWidth())
        self.deviceUrlLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.deviceUrlLabel.setFont(font)
        self.deviceUrlLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.deviceUrlLabel.setObjectName("deviceUrlLabel")
        self.gridLayout.addWidget(self.deviceUrlLabel, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.reconnectButton = QtWidgets.QPushButton(CameraView)
        self.reconnectButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.reconnectButton.sizePolicy().hasHeightForWidth())
        self.reconnectButton.setSizePolicy(sizePolicy)
        self.reconnectButton.setObjectName("reconnectButton")
        self.gridLayout.addWidget(self.reconnectButton, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.cameraResolutionLabel = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cameraResolutionLabel.sizePolicy().hasHeightForWidth())
        self.cameraResolutionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cameraResolutionLabel.setFont(font)
        self.cameraResolutionLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.cameraResolutionLabel.setObjectName("cameraResolutionLabel")
        self.gridLayout.addWidget(self.cameraResolutionLabel, 2, 1, 1, 1)
        self.clearImageBufferButton = QtWidgets.QPushButton(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clearImageBufferButton.sizePolicy().hasHeightForWidth())
        self.clearImageBufferButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.clearImageBufferButton.setFont(font)
        self.clearImageBufferButton.setObjectName("clearImageBufferButton")
        self.gridLayout.addWidget(self.clearImageBufferButton, 7, 3, 1, 1)
        self.nFramesProcessedLabel = QtWidgets.QLabel(CameraView)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nFramesProcessedLabel.sizePolicy().hasHeightForWidth())
        self.nFramesProcessedLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.nFramesProcessedLabel.setFont(font)
        self.nFramesProcessedLabel.setText("")
        self.nFramesProcessedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nFramesProcessedLabel.setObjectName("nFramesProcessedLabel")
        self.gridLayout.addWidget(self.nFramesProcessedLabel, 4, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(CameraView)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(CameraView)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(CameraView)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(CameraView)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(CameraView)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(CameraView)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(CameraView)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(CameraView)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(CameraView)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 0, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(CameraView)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(CameraView)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 2, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(CameraView)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 1, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(CameraView)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 2, 3, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_12 = QtWidgets.QLabel(CameraView)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(CameraView)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(CameraView)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(CameraView)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.Version = QtWidgets.QLabel(CameraView)
        self.Version.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Version.setObjectName("Version")
        self.verticalLayout.addWidget(self.Version)
        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(CameraView)
        QtCore.QMetaObject.connectSlotsByName(CameraView)

    def retranslateUi(self, CameraView):
        _translate = QtCore.QCoreApplication.translate
        CameraView.setWindowTitle(_translate("CameraView", "Form"))
        self.label_8.setText(_translate(
            "CameraView", "Description function camera"))
        self.label_4.setText(_translate("CameraView", "Camera Device Url:"))
        self.startButton.setText(_translate("CameraView", "Start"))
        self.pauseButton.setText(_translate("CameraView", "Pause"))
        self.label_2.setText(_translate("CameraView", "Capture Rate:"))
        self.label_3.setText(_translate("CameraView", "Processing Rate:"))
        self.label_1.setText(_translate("CameraView", "Image Buffer:"))
        self.label_7.setText(_translate("CameraView", "Cursor:"))
        self.label_5.setText(_translate("CameraView", "Camera Resolution:"))
        self.reconnectButton.setText(_translate("CameraView", "Reconnect"))
        self.label_6.setText(_translate("CameraView", "ROI:"))
        self.clearImageBufferButton.setText(
            _translate("CameraView", "Clear Image Buffer"))
        self.label.setText(_translate("CameraView", " Vehicle tracking"))
        self.label_9.setText(_translate("CameraView", "Taxi:"))
        self.label_15.setText(_translate("CameraView", "0"))
        self.label_16.setText(_translate("CameraView", "0"))
        self.label_17.setText(_translate("CameraView", "Motobike:"))
        self.label_14.setText(_translate("CameraView", "0"))
        self.label_13.setText(_translate("CameraView", "Truck:"))
        self.label_10.setText(_translate("CameraView", "Bus:"))
        self.label_18.setText(_translate("CameraView", "0"))
        self.label_19.setText(_translate("CameraView", "Police:"))
        self.label_20.setText(_translate("CameraView", "Ambulance:"))
        self.label_21.setText(_translate("CameraView", "0"))
        self.label_22.setText(_translate("CameraView", "0"))
        self.label_12.setText(_translate("CameraView", "Other:"))
        self.label_11.setText(_translate("CameraView", "Error: "))
        self.label_23.setText(_translate("CameraView", "0"))
        self.label_24.setText(_translate("CameraView", "Null"))
        self.Version.setText(_translate("CameraView", "Version: 2.2.3"))
