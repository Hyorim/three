#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import time
import json
import datetime
import urllib.request
import pygame
import threading
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QDate,QTime,Qt
from urllib.request import urlopen
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QLabel
from threading import Timer
from pytz import timezone
from datetime import datetime
from PyMata.pymata import PyMata

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        global _translate
        _translate = QtCore.QCoreApplication.translate


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800,440)

        
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        self.main_frame = QtWidgets.QFrame(self.centralWidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 800, 440))
 
        self.main_label = QtWidgets.QLabel(self.main_frame)
        self.main_label.setGeometry(QtCore.QRect(0, 0, 800, 440))
        self.main_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_label.setObjectName("main_label")


        main_pixmap=QPixmap("./image/background.png")
        self.main_label.setPixmap(QPixmap(main_pixmap))


#List Icon, country name
        self.list_pushButton = QtWidgets.QPushButton(self.main_frame)
        self.list_pushButton.setGeometry(QtCore.QRect(30, 20, 50, 50))
        self.list_pushButton.setObjectName("list_pushButton")

        self.list_pushButton.setStyleSheet('image:url(./image/list.png);border:0px;')

        self.cityname_label = QtWidgets.QLabel(self.main_frame)
        self.cityname_label.setGeometry(QtCore.QRect(100, 25, 440, 50))
        self.cityname_label.setObjectName("country_label")
        self.cityname_label.setStyleSheet("color:white; font:thin;")



#==========

#Temp


        self.temp_img_label = QtWidgets.QLabel(self.main_frame) 
        self.temp_img_label.setGeometry(QtCore.QRect(85, 102,120, 120))
        self.temp_img_label.setObjectName("temp_img_label")

        temp_pixmap=QPixmap("./image/temp.png")
        self.temp_img_label.setScaledContents(True)
        self.temp_img_label.setPixmap(QPixmap(temp_pixmap))


        self.temp_label = QtWidgets.QLabel(self.main_frame)
        self.temp_label.setGeometry(QtCore.QRect(118,226,45,35))
        self.temp_label.setObjectName("temp_label")
        self.temp_label.setStyleSheet("color:white;")
        self.temp_label.setAlignment(Qt.AlignRight)
 

        self.degree_label = QtWidgets.QLabel(self.main_frame)
        self.degree_label.setGeometry(QtCore.QRect(165,223,30,35))
        self.degree_label.setObjectName("degree_label")
        self.degree_label.setStyleSheet("color:white; font:bold;")





#Weather,Time,Date
        self.weather_label = QtWidgets.QLabel(self.main_frame)
        self.weather_label.setGeometry(QtCore.QRect(300,220,218,45))
        self.weather_label.setObjectName("weather_label")
        self.weather_label.setStyleSheet("color:white;")
        self.weather_label.setAlignment(Qt.AlignCenter)



        self.weather_img_label = QtWidgets.QLabel(self.main_frame)
        self.weather_img_label.setGeometry(QtCore.QRect(358,121,100,100))
        self.weather_img_label.setObjectName("weather_img_label")

        weather_pixmap=QPixmap("./image/sunny.png")
        self.weather_img_label.setPixmap(QPixmap(weather_pixmap))
        self.weather_img_label.setScaledContents(True)
 
        self.date_label = QtWidgets.QLabel(self.main_frame)
        self.date_label.setGeometry(QtCore.QRect(528,143,230,35))
        self.date_label.setObjectName("date_label")
        self.date_label.setAlignment(Qt.AlignRight)
        self.date_label.setStyleSheet("color:white;")


        self.time_label = QtWidgets.QLabel(self.main_frame)
        self.time_label.setGeometry(QtCore.QRect(528,196,230,35))
        self.time_label.setObjectName("time_label")
        self.time_label.setAlignment(Qt.AlignRight)
        self.time_label.setStyleSheet("color:white;")



#Need Frame, Icon


        self.need_back_label = QtWidgets.QLabel(self.main_frame)
        self.need_back_label.setGeometry(QtCore.QRect(205, 280, 390, 140))
        self.need_back_label.setObjectName("need_back_label")
 
        need_back_pixmap=QPixmap("./image/need_background.png")
        self.need_back_label.setPixmap(QPixmap(need_back_pixmap))
        self.need_back_label.setScaledContents(True) 

        self.need_img_label = QtWidgets.QLabel(self.main_frame)
        self.need_img_label.setGeometry(QtCore.QRect(350, 324, 90, 90))
        self.need_img_label.setObjectName("need_img_label")
        self.need_img_label.setScaledContents(True)


#==========

#==========
#World Map Frame

 
        self.map_frame = QtWidgets.QFrame(self.centralWidget)
        self.map_frame.setGeometry(QtCore.QRect(0, 0, 800, 440))
        self.map_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.map_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.map_frame.setObjectName("map_frame")


        self.map_img_label = QtWidgets.QLabel(self.map_frame)
        self.map_img_label.setGeometry(QtCore.QRect(0, 0, 800, 440))
        self.map_img_label.setObjectName("map_img_label")
 
        map_img_pixmap=QPixmap("./image/map.png")
        self.map_img_label.setPixmap(QPixmap(map_img_pixmap))




        self.seoul_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.seoul_pushButton.setGeometry(QtCore.QRect(618,147, 50, 33))
        self.seoul_pushButton.setObjectName("seoul_pushButton")
        self.seoul_pushButton.setStyleSheet('image:url(./image/seoul.png);border:0px;')


        self.bangkok_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.bangkok_pushButton.setGeometry(QtCore.QRect(557, 201, 50, 33))
        self.bangkok_pushButton.setObjectName("bangkok_pushButton")
        self.bangkok_pushButton.setStyleSheet('image:url(./image/bangkok.png);border:0px;')


        self.berlin_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.berlin_pushButton.setGeometry(QtCore.QRect(373, 117, 50, 33))
        self.berlin_pushButton.setObjectName("berlin_pushButton")
        self.berlin_pushButton.setStyleSheet('image:url(./image/berlin.png);border:0px;')


        self.bogota_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.bogota_pushButton.setGeometry(QtCore.QRect(181, 223, 50, 33))
        self.bogota_pushButton.setObjectName("bogota_pushButton")
        self.bogota_pushButton.setStyleSheet('image:url(./image/bogota.png);border:0px;')


        self.cairo_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.cairo_pushButton.setGeometry(QtCore.QRect(410, 175, 50, 33))
        self.cairo_pushButton.setObjectName("cairo_pushButton")
        self.cairo_pushButton.setStyleSheet('image:url(./image/cairo.png);border:0px;')


        self.dublin_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.dublin_pushButton.setGeometry(QtCore.QRect(310, 130, 50, 33))
        self.dublin_pushButton.setObjectName("dublin_pushButton")
        self.dublin_pushButton.setStyleSheet('image:url(./image/dublin.png);border:0px;')


        self.honolulu_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.honolulu_pushButton.setGeometry(QtCore.QRect(28, 195, 50, 33))
        self.honolulu_pushButton.setObjectName("honolulu_pushButton")
        self.honolulu_pushButton.setStyleSheet('image:url(./image/honolulu.png);border:0px;')


        self.london_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.london_pushButton.setGeometry(QtCore.QRect(321, 91, 50, 33))
        self.london_pushButton.setObjectName("london_pushButton")
        self.london_pushButton.setStyleSheet('image:url(./image/london.png);border:0px;')

        self.madrid_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.madrid_pushButton.setGeometry(QtCore.QRect(341, 165, 50, 33))
        self.madrid_pushButton.setObjectName("madrid_pushButton")
        self.madrid_pushButton.setStyleSheet('image:url(./image/madrid.png);border:0px;')


        self.moscow_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.moscow_pushButton.setGeometry(QtCore.QRect(445, 115, 50, 33))
        self.moscow_pushButton.setObjectName("moscow_pushButton")
        self.moscow_pushButton.setStyleSheet('image:url(./image/moscow.png);border:0px;')

        self.nairobi_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.nairobi_pushButton.setGeometry(QtCore.QRect(424, 235, 50, 33))
        self.nairobi_pushButton.setObjectName("nairobi_pushButton")
        self.nairobi_pushButton.setStyleSheet('image:url(./image/nairobi.png);border:0px;')


        self.newyork_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.newyork_pushButton.setGeometry(QtCore.QRect(200, 148, 50, 33))
        self.newyork_pushButton.setObjectName("newyork_pushButton")
        self.newyork_pushButton.setStyleSheet('image:url(./image/newyork.png);border:0px;')

        self.sydney_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.sydney_pushButton.setGeometry(QtCore.QRect(668, 279, 50, 33))
        self.sydney_pushButton.setObjectName("sydney_pushButton")
        self.sydney_pushButton.setStyleSheet('image:url(./image/sydney.png);border:0px;')


        self.taipei_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.taipei_pushButton.setGeometry(QtCore.QRect(460, 277, 50, 33))
        self.taipei_pushButton.setObjectName("taipei_pushButton")
        self.taipei_pushButton.setStyleSheet('image:url(./image/taipei.png);border:0px;')

        self.tokyo_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.tokyo_pushButton.setGeometry(QtCore.QRect(672, 156, 50, 33))
        self.tokyo_pushButton.setObjectName("tokyo_pushButton")
        self.tokyo_pushButton.setStyleSheet('image:url(./image/tokyo.png);border:0px;')

        self.vancouver_pushButton = QtWidgets.QPushButton(self.map_frame)
        self.vancouver_pushButton.setGeometry(QtCore.QRect(78, 133, 50, 33))
        self.vancouver_pushButton.setObjectName("vancouver_pushButton")
        self.vancouver_pushButton.setStyleSheet('image:url(./image/vancouver.png);border:0px;')


#==========

        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        global country_name
        global weather_font
        weather_font = QtGui.QFont("impact")
        weather_font.setPointSize(20)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather Information"))
        self.degree_label.setText(_translate("MainWindow","℃"))
        self.degree_label.setFont(weather_font)

        self.main_frame.hide()

        self.resetButtons()
            


#=====
      
#Clicked Method
 
        self.list_pushButton.clicked.connect(self.clickList)

        self.bangkok_pushButton.clicked.connect(self.clickBangkok)
        self.berlin_pushButton.clicked.connect(self.clickBerlin)
        self.bogota_pushButton.clicked.connect(self.clickBogota)
        self.cairo_pushButton.clicked.connect(self.clickCairo)
        self.dublin_pushButton.clicked.connect(self.clickDublin)
        self.honolulu_pushButton.clicked.connect(self.clickHonolulu)
        self.london_pushButton.clicked.connect(self.clickLondon)
        self.madrid_pushButton.clicked.connect(self.clickMadrid)
        self.moscow_pushButton.clicked.connect(self.clickMoscow)
        self.nairobi_pushButton.clicked.connect(self.clickNairobi)
        self.newyork_pushButton.clicked.connect(self.clickNewyork)
        self.seoul_pushButton.clicked.connect(self.clickSeoul)
        self.sydney_pushButton.clicked.connect(self.clickSydney)
        self.taipei_pushButton.clicked.connect(self.clickTaipei)
        self.tokyo_pushButton.clicked.connect(self.clickTokyo)
        self.vancouver_pushButton.clicked.connect(self.clickVancouver)

#set motor board
        global board
        try:
            board = PyMata('/dev/ttyACM0')
        except SerialTimeoutException:
            log.exception("error")


        global fog_pin
        fog_pin = 4
        board.set_pin_mode(fog_pin, board.OUTPUT, board.DIGITAL)
        board.digital_write(fog_pin,0)

        global wind_dir,wind_speed
        wind_dir = 12
        wind_speed = 10
            
        board.set_pin_mode(wind_speed, board.PWM, board.DIGITAL)
        board.set_pin_mode(wind_dir, board.OUTPUT, board.DIGITAL)

        board.digital_write(wind_dir,0)
        board.analog_write(wind_speed, 0);
        
        global rain_dir,rain_speed
        rain_dir = 13
        rain_speed = 11

        board.set_pin_mode(rain_speed, board.PWM, board.DIGITAL)
        board.set_pin_mode(rain_dir, board.OUTPUT, board.DIGITAL)

        board.digital_write(rain_dir,1)
        board.analog_write(rain_speed, 0);


#set lights
        global sand_l,dust_l,thunder_l,day_l,spring_l,summer_l,winter_l 
        sand_l=2
        dust_l=3
        thunder_l=5
        day_l=6
        spring_l=7
        summer_l=8
        winter_l=9

        sleep(1)
        board.set_pin_mode(sand_l,board.OUTPUT,board.DIGITAL)
        board.set_pin_mode(dust_l,board.OUTPUT,board.DIGITAL)
        sleep(1)
        board.set_pin_mode(thunder_l,board.OUTPUT,board.DIGITAL)
        board.set_pin_mode(day_l,board.OUTPUT,board.DIGITAL)
        sleep(1)
        board.set_pin_mode(spring_l,board.OUTPUT,board.DIGITAL)
        board.set_pin_mode(summer_l,board.OUTPUT,board.DIGITAL)
        board.set_pin_mode(winter_l,board.OUTPUT,board.DIGITAL)

#        board.analog_write(wind_speed, 80);
        global flag_rain
        flag_rain=0
        global flag_thunder
        flag_thunder=0
        global flag_clear, flag_clouds, flag_drizzle
        flag_clear=0
        flag_clouds=0
        flag_drizzle=0
        self.reset_motor()

    def reset_motor(self):
        global board
#        try:
#            board = PyMata('/dev/ttyACM0')
#        except SerialTimeoutException:
#            log.exception("error")
 

        global wind_dir,wind_speed
        wind_dir = 12
        wind_speed = 10

        board.set_pin_mode(wind_speed, board.PWM, board.DIGITAL)
        board.set_pin_mode(wind_dir, board.OUTPUT, board.DIGITAL)

        board.digital_write(wind_dir,0)
        board.analog_write(wind_speed, 0)

        global rain_dir, rain_speed
        rain_dir = 13
        rain_speed = 11

        board.set_pin_mode(rain_speed, board.PWM, board.DIGITAL)
        board.set_pin_mode(rain_dir, board.OUTPUT, board.DIGITAL)

        board.digital_write(rain_dir,1)
        board.analog_write(rain_speed, 0)


        sleep(1)
        global sand_l,dust_l,thunder_l,day_l,spring_l,summer_l,winter_l
        board.digital_write(sand_l,0)
        board.digital_write(dust_l,0)
        sleep(1)
        board.digital_write(thunder_l,0)
        board.digital_write(day_l,0)
        sleep(1)
        board.digital_write(spring_l,0)
        board.digital_write(summer_l,0)
        board.digital_write(winter_l,0)

        #global fog_board
        global fog_pin
        board.digital_write(fog_pin,0)

        global flag_rain
        if flag_rain == 1:
            global rain_timer
            rain_timer.cancel()
            flag_rain=0
            pygame.mixer.music.stop()

        global flag_thunder
        if flag_thunder == 1:
            global thunder_timer,thunder_l_timer
            thunder_timer.cancel()
            thunder_l_timer.cancel()
            flag_thunder=0
            pygame.mixer.music.stop()

        global flag_clear
        if flag_clear == 1:
            global clear_timer
            clear_timer.cancel()
            flag_clear=0
            pygame.mixer.music.stop()


        global flag_clouds
        if flag_clouds == 1:
            global clouds_timer
            clouds_timer.cancel()
            flag_clouds=0
            pygame.mixer.music.stop()


        global flag_drizzle
        if flag_drizzle == 1:
            global drizzle_timer
            drizzle_timer.cancel()
            flag_drizzle=0
            pygame.mixer.music.stop()


    def clickList(self):
        global timer
        timer.cancel()
        self.map_frame.show()
        self.main_frame.hide()

        self.reset_motor()


    def resetButtons(self):
        self.bangkok_pushButton.setText(_translate("MainWindow"," "))
        self.bangkok_pushButton.setStyleSheet('image:url(./image/bangkok.png);border:0px;')
        self.berlin_pushButton.setText(_translate("MainWindow"," "))
        self.berlin_pushButton.setStyleSheet('image:url(./image/berlin.png);border:0px;')
        self.bogota_pushButton.setText(_translate("MainWindow"," "))
        self.bogota_pushButton.setStyleSheet('image:url(./image/bogota.png);border:0px;')
        self.cairo_pushButton.setText(_translate("MainWindow"," "))
        self.cairo_pushButton.setStyleSheet('image:url(./image/cairo.png);border:0px;')
        self.dublin_pushButton.setText(_translate("MainWindow"," "))
        self.dublin_pushButton.setStyleSheet('image:url(./image/dublin.png);border:0px;')
        self.honolulu_pushButton.setText(_translate("MainWindow"," "))
        self.honolulu_pushButton.setStyleSheet('image:url(./image/honolulu.png);border:0px;')
        self.london_pushButton.setText(_translate("MainWindow"," "))
        self.london_pushButton.setStyleSheet('image:url(./image/london.png);border:0px;')
        self.madrid_pushButton.setText(_translate("MainWindow"," "))
        self.madrid_pushButton.setStyleSheet('image:url(./image/madrid.png);border:0px;')
        self.moscow_pushButton.setText(_translate("MainWindow"," "))
        self.moscow_pushButton.setStyleSheet('image:url(./image/moscow.png);border:0px;')
        self.nairobi_pushButton.setText(_translate("MainWindow"," "))
        self.nairobi_pushButton.setStyleSheet('image:url(./image/nairobi.png);border:0px;')
        self.newyork_pushButton.setText(_translate("MainWindow"," "))
        self.newyork_pushButton.setStyleSheet('image:url(./image/newyork.png);border:0px;')
        self.seoul_pushButton.setText(_translate("MainWindow"," "))
        self.seoul_pushButton.setStyleSheet('image:url(./image/seoul.png);border:0px;')
        self.sydney_pushButton.setText(_translate("MainWindow"," "))
        self.sydney_pushButton.setStyleSheet('image:url(./image/sydney.png);border:0px;')
        self.taipei_pushButton.setText(_translate("MainWindow"," "))
        self.taipei_pushButton.setStyleSheet('image:url(./image/taipei.png);border:0px;')
        self.tokyo_pushButton.setText(_translate("MainWindow"," "))
        self.tokyo_pushButton.setStyleSheet('image:url(./image/tokyo.png);border:0px;')
        self.vancouver_pushButton.setText(_translate("MainWindow"," "))
        self.vancouver_pushButton.setStyleSheet('image:url(./image/vancouver.png);border:0px;')

    def changeFrame(self):
        global country_name
        self.getWeather(country_name)
        self.map_frame.hide()
        self.main_frame.show()

        self.update_time()
             

    def clickBangkok(self):
        global country_name
        if self.bangkok_pushButton.text()==' ':
           self.resetButtons()
           self.bangkok_pushButton.setText("Bangkok")
           self.bangkok_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.bangkok_pushButton.setText(" ")
           self.bangkok_pushButton.setStyleSheet('image:url(./image/bangkok.png);border:0px;') 
           country_name = 'Bangkok'
           self.changeFrame()

    def clickBerlin(self):
        global country_name
        if self.berlin_pushButton.text()==' ':
           self.resetButtons()
           self.berlin_pushButton.setText("Berlin")
           self.berlin_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.berlin_pushButton.setText(" ")
           self.berlin_pushButton.setStyleSheet('image:url(./image/berlin.png);border:0px;')
           country_name = 'Berlin'
           self.changeFrame()

    def clickBogota(self):
        global country_name
        if self.bogota_pushButton.text()==' ':
           self.resetButtons()
           self.bogota_pushButton.setText("Bogota")
           self.bogota_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.bogota_pushButton.setText(" ")
           self.bogota_pushButton.setStyleSheet('image:url(./image/bogota.png);border:0px;')
           country_name = 'Bogota'
           self.changeFrame()

    def clickCairo(self):
        global country_name
        if self.cairo_pushButton.text()==' ':
           self.resetButtons()
           self.cairo_pushButton.setText("Cairo")
           self.cairo_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.cairo_pushButton.setText(" ")
           self.cairo_pushButton.setStyleSheet('image:url(./image/cairo.png);border:0px;')
           country_name = 'Cairo'
           self.changeFrame()

    def clickDublin(self):
        global country_name
        if self.dublin_pushButton.text()==' ':
           self.resetButtons()
           self.dublin_pushButton.setText("Dublin")
           self.dublin_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.dublin_pushButton.setText(" ")
           self.dublin_pushButton.setStyleSheet('image:url(./image/dublin.png);border:0px;')
           country_name = 'Dublin'
           self.changeFrame()

    def clickHonolulu(self):
        global country_name
        if self.honolulu_pushButton.text()==' ':
           self.resetButtons()
           self.honolulu_pushButton.setText("Honolulu")
           self.honolulu_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.honolulu_pushButton.setText(" ")
           self.honolulu_pushButton.setStyleSheet('image:url(./image/honolulu.png);border:0px;')
           country_name = 'Honolulu'
           self.changeFrame()

    def clickLondon(self):
        global country_name
        if self.london_pushButton.text()==' ':
           self.resetButtons()
           self.london_pushButton.setText("London")
           self.london_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.london_pushButton.setText(" ")
           self.london_pushButton.setStyleSheet('image:url(./image/london.png);border:0px;')
           country_name ='London'
           self.changeFrame()

    def clickMadrid(self):
        global country_name
        if self.madrid_pushButton.text()==' ':
           self.resetButtons()
           self.madrid_pushButton.setText("Madrid")
           self.madrid_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.madrid_pushButton.setText(" ")
           self.madrid_pushButton.setStyleSheet('image:url(./image/madrid.png);border:0px;')
           country_name = 'Madrid'
           self.changeFrame()

    def clickMoscow(self):
        global country_name
        if self.moscow_pushButton.text()==' ':
           self.resetButtons()
           self.moscow_pushButton.setText("Moscow")
           self.moscow_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.moscow_pushButton.setText(" ")
           self.moscow_pushButton.setStyleSheet('image:url(./image/moscow.png);border:0px;')
           country_name ='Moscow'
           self.changeFrame()

    def clickNairobi(self):
        global country_name
        if self.nairobi_pushButton.text()==' ':
           self.resetButtons()
           self.nairobi_pushButton.setText("Nairobi")
           self.nairobi_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.nairobi_pushButton.setText(" ")
           self.nairobi_pushButton.setStyleSheet('image:url(./image/nairobi.png);border:0px;')
           country_name = 'Nairobi'
           self.changeFrame()

    def clickNewyork(self):
        global country_name
        if self.newyork_pushButton.text()==' ':
           self.resetButtons()
           self.newyork_pushButton.setText("Newyork")
           self.newyork_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.newyork_pushButton.setText(" ")
           self.newyork_pushButton.setStyleSheet('image:url(./image/newyork.png);border:0px;')
           country_name = 'NewYork'
           self.changeFrame()

    def clickSeoul(self):
        global country_name
        if self.seoul_pushButton.text()==' ':
           self.resetButtons()
           self.seoul_pushButton.setText("Seoul")
           self.seoul_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.seoul_pushButton.setText(" ")
           self.seoul_pushButton.setStyleSheet('image:url(./image/seoul.png);border:0px;')
           country_name = 'Seoul'
           self.changeFrame()

    def clickSydney(self):
        global country_name
        if self.sydney_pushButton.text()==' ':
           self.resetButtons()
           self.sydney_pushButton.setText("Sydney")
           self.sydney_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.sydney_pushButton.setText(" ")
           self.sydney_pushButton.setStyleSheet('image:url(./image/sydney.png);border:0px;')
           country_name = 'Sydney'
           self.changeFrame()

    def clickTaipei(self):
        global country_name
        if self.taipei_pushButton.text()==' ':
           self.resetButtons()
           self.taipei_pushButton.setText("Taipei")
           self.taipei_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.taipei_pushButton.setText(" ")
           self.taipei_pushButton.setStyleSheet('image:url(./image/taipei.png);border:0px;')
           country_name = 'Taipei'
           self.changeFrame()

    def clickTokyo(self):
        global country_name
        if self.tokyo_pushButton.text()==' ':
           self.resetButtons()
           self.tokyo_pushButton.setText("Tokyo")
           self.tokyo_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.tokyo_pushButton.setText(" ")
           self.tokyo_pushButton.setStyleSheet('image:url(./image/tokyo.png);border:0px;')
           country_name = 'Tokyo'
           self.changeFrame()

    def clickVancouver(self):
        global country_name
        if self.vancouver_pushButton.text()==' ':
           self.resetButtons()
           self.vancouver_pushButton.setText("Vancouver")
           self.vancouver_pushButton.setStyleSheet('background-color:white; border:0px; font:bold;')
        else:
           self.vancouver_pushButton.setText(" ")
           self.vancouver_pushButton.setStyleSheet('image:url(./image/vancouver.png);border:0px;')
           country_name = 'Vancouver'
           self.changeFrame()

#Clicked Flags


       
#==========

#WebParsing

    def country_weather(self,weather,nation):
        #_translate = QtCore.QCoreApplication.translate
        global weather_font
        global board
        global sand_l,dust_l,thunder_l,day_l,spring_l,summer_l,winter_l
        global wind_dir,wind_speed

        global fog_board
        global fog_pin

        weather_arr=[];
        weather_=weather["weather"];
       

        temp=round(weather["main"]["temp"]-273.15);
        self.temp_label.setText(_translate("MainWindow",str(temp)))
        self.temp_label.setFont(weather_font)


        wind=weather["wind"]["speed"];
        if temp<10:
         weather_arr.append('winter')
         board.digital_write(winter_l,1)
        elif 10<=temp<25:
         weather_arr.append('spring')
         board.digital_write(spring_l,1)
        else:
         weather_arr.append('summer')
         board.digital_write(summer_l,1)

        Bangkok=datetime.now(timezone('Asia/Bangkok'))
        Seoul=datetime.now(timezone('Asia/Seoul'))      
        Taipei=datetime.now(timezone('Asia/Taipei'))
        Tokyo=datetime.now(timezone('Asia/Tokyo'))
        Nairobi=datetime.now(timezone('Africa/Nairobi'))
        Cairo=datetime.now(timezone('Africa/Cairo'))
        Berlin=datetime.now(timezone('Europe/Berlin'))
        Dublin=datetime.now(timezone('Europe/Dublin'))
        London=datetime.now(timezone('Europe/London'))
        Madrid=datetime.now(timezone('Europe/Madrid'))
        Moscow=datetime.now(timezone('Europe/Moscow'))
        Bogota=datetime.now(timezone('America/Bogota'))
        Sydney=datetime.now(timezone('Australia/Sydney'))
        Vancouver=datetime.now(timezone('America/Vancouver'))
        New_York=datetime.now(timezone('America/New_York'))
        Honolulu=datetime.now(timezone('Pacific/Honolulu'))


        time=[];
        fmt = "%Y-%m-%d %H:%M:%S"
        if nation=="Bangkok":
                time=Bangkok.strftime(fmt);
        if nation=="Seoul":
                time=Seoul.strftime(fmt);
        if nation=="Taipei":
                time=Taipei.strftime(fmt);
        if nation=="Tokyo":
                time=Tokyo.strftime(fmt);
        if nation=="Nairobi":
                time=Nairobi.strftime(fmt);
        if nation=="Cairo":
                time=Cairo.strftime(fmt);
        if nation=="Berlin":
                time=Berlin.strftime(fmt);
        if nation=="Dublin":
                time=Dublin.strftime(fmt);
        if nation=="London":
               time=London.strftime(fmt);
        if nation=="Madrid":
                time=Madrid.strftime(fmt);
        if nation=="Moscow":
                time=Moscow.strftime(fmt);
        if nation=="Bogota":
                time=Bogota.strftime(fmt);
        if nation=="Sydney":
                time=Sydney.strftime(fmt);
        if nation=="Vancouver":
                time=Vancouver.strftime(fmt);
        if nation=="NewYork":
                time=New_York.strftime(fmt);
        if nation=="Honolulu":
                time=Honolulu.strftime(fmt);


        self.date_label.setText(_translate("MainWindow",time[0:4]+"년"+time[5:7]+"월"+time[8:10]+"일"))
#        self.date_label.setFont(weather_font)
        self.date_label.setStyleSheet("color:white; font-size:20pt; font:bold;")

        self.time_label.setText(_translate("MainWindow",time[11:13]+"시"+time[14:16]+"분"+time[17:19]+"초"))
 #       self.time_label.setFont(weather_font)
        self.time_label.setStyleSheet("color:white; font-size:20pt; font:bold;")


        global day_l
        temp_hour=(int(time[11])*10)+int(time[12])
        if temp_hour >= 9 and temp_hour <18:
            board.digital_write(day_l,1)



        global hour_g
        global min_g
        global sec_g
        hour_g=int(time[11:13])
        min_g=int(time[14:16])
        sec_g=int(time[17:19])



        weather_arr.append(time);
        main=weather["weather"][0]["main"];

#Light Test
#        main="Thunderstorm"
#        board.digital_write(dust_l,1)
#        board.digital_write(thunder_l,1)
#        board.digital_write(sand_l,1)


        desc=weather_[0]["description"];
        weather_arr.append(temp);
        weather_arr.append(main);
        main_=weather["weather"]
        self.weather_label.setText(_translate("MainWindow",main))
        self.weather_label.setFont(weather_font)

        current_dec=main_[0]["description"]




#Change need and weather icon
        need_img_pixmap=QPixmap("./image/none.png")
        self.need_img_label.setPixmap(QPixmap(need_img_pixmap))


        if main =="Clear":
           need_img_pixmap=QPixmap("./image/sunglass.png")
           self.need_img_label.setPixmap(QPixmap(need_img_pixmap))
           weather_pixmap=QPixmap("./image/sunny.png")
           self.weather_img_label.setPixmap(QPixmap(weather_pixmap))

           if temp>25:
              need_img_pixmap=QPixmap("./image/fan.png")
              self.need_img_label.setPixmap(QPixmap(need_img_pixmap))

           global flag_clear
           flag_clear=1
           global clear_timer
           self.clear_sound()





        if main =="Clouds":
           weather_pixmap=QPixmap("./image/cloudy.png")
           self.weather_img_label.setPixmap(QPixmap(weather_pixmap))
           global flag_clouds
           flag_clouds=1
           global clouds_timer
           self.clouds_sound()




        if main=="Snow":
           need_img_pixmap=QPixmap("./image/glove.png")
           self.need_img_label.setPixmap(QPixmap(need_img_pixmap))
           weather_pixmap=QPixmap("./image/snow.png")
           self.weather_img_label.setPixmap(QPixmap(weather_pixmap))

           if current_dec=="light snow":
              weather_arr.append(1);
           else:
              weather_arr.append(3);
        else:
           weather_arr.append(0);

        if main =="Thunderstorm":
           weather_pixmap=QPixmap("./image/thunder.png")
           self.weather_img_label.setPixmap(QPixmap(weather_pixmap))
           board.digital_write(thunder_l,1)
           global flag_thunder
           flag_thunder=1
           global thunder_timer
           self.thunder_sound()
           self.thunder_light()

        if main =="Dust":
           need_img_pixmap=QPixmap("./image/mask.png")
           self.need_img_label.setPixmap(QPixmap(need_img_pixmap))

           

           board.digital_write(dust_l,1)
           board.digital_write(fog_pin,1)

        global rain_speed

        if main=="Rain":
           need_img_pixmap=QPixmap("./image/umbrella.png")
           self.need_img_label.setPixmap(QPixmap(need_img_pixmap))
           weather_pixmap=QPixmap("./image/rainy.png")
           self.weather_img_label.setPixmap(QPixmap(weather_pixmap)) 
           board.analog_write(rain_speed,255)
           global flag_rain
           flag_rain=1

           global rain_timer
           self.rain_sound()

           if current_dec=="light intensity shower rain":
              weather_arr.append(1)
           else:  
              weather_arr.append(3)

        elif main=="Drizzle":
           need_img_pixmap=QPixmap("./image/umbrella.png")
           self.need_img_label.setPixmap(QPixmap(need_img_pixmap))
           weather_pixmap=QPixmap("./image/rainy.png")
           self.weather_img_label.setPixmap(QPixmap(weather_pixmap))
           board.analog_write(rain_speed,255)
           weather_arr.append(1)

           global flag_drizzle
           flag_drizzle=1

           global drizzle_timer
           self.drizzle_sound()

        else:
           weather_arr.append(0);
    

        if main=="Fog" or main=="Mist" or main=="Haze" or main=="Smoke":
           weather_pixmap=QPixmap("./image/fog.png")
           self.weather_img_label.setPixmap(QPixmap(weather_pixmap))
           board.digital_write(fog_pin,1)


#======

#wind speed


        board.digital_write(wind_dir,0)

        if int(wind)<=1:
           weather_arr.append(1)
           board.analog_write(wind_speed, 80);
        elif 1<int(wind)<=3:
           weather_arr.append(2)
           board.analog_write(wind_speed,120);
        else:
           weather_arr.append(3)
           board.analog_write(wind_speed,250);

        global country_name
        self.cityname_label.setText(country_name)
        cityname_font = QtGui.QFont("impact")
        cityname_font.setPointSize(30)
        self.cityname_label.setFont(cityname_font)


    def getWeather(self,name):
        a=name
        if a=='NewYork':
           a='New%20York'

        url='http://api.openweathermap.org/data/2.5/weather?q='+a+'&APPID=990cae6ed2b0f4059dc52bbe460873f5'
        data=urllib.request.urlopen(url)
        weather=data.read()
        j=json.loads(weather.decode('utf-8'))
        main=j["weather"]
        current=main[0]["main"]
        current_dec=main[0]["description"]
        temp=j["main"]
        current_temp=temp["temp"]-273.15
        timeT=j["dt"]


        if a=='New%20York':
           a='NewYork'
        self.country_weather(j,a)

#Rain Sound
    def rain_sound(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("rain.mp3")
        pygame.mixer.music.play()

        global rain_timer
        rain_timer=threading.Timer(60,self.rain_sound)
        rain_timer.start()

#Thunder Sound
    def thunder_sound(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("thunder.mp3")
        pygame.mixer.music.play()

        global thunder_timer
        thunder_timer=threading.Timer(60,self.thunder_sound)
        thunder_timer.start()


#Thunder Light
    def thunder_light(self):
        global board
        global thunder_l
        board.digital_write(thunder_l,1)
        time.sleep(0.5)
        board.digital_write(thunder_l,0)
        time.sleep(0.5)
        global thunder_l_timer
        thunder_l_timer=threading.Timer(1,self.thunder_light)
        thunder_l_timer.start()

#Clear Sound
    def clear_sound(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("clear.mp3")
        pygame.mixer.music.play()

        global clear_timer
        clear_timer=threading.Timer(60,self.clear_sound)
        clear_timer.start()


#Clouds Sound
    def clouds_sound(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("clouds.mp3")
        pygame.mixer.music.play()
     
        global clouds_timer
        clouds_timer=threading.Timer(60,self.clouds_sound)
        clouds_timer.start()


#Drizzle Sound
    def drizzle_sound(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("drizzle.mp3")
        pygame.mixer.music.play()
     
        global drizzle_timer
        drizzle_timer=threading.Timer(60,self.drizzle_sound)
        drizzle_timer.start()




#Update Time
    def update_time(self):
        _translate = QtCore.QCoreApplication.translate
        global hour_g,min_g,sec_g

        global timer
        timer=Timer(1,self.update_time)
        timer.start()

        self.next_sec()
        self.time_label.setText(_translate("MainWindow",str(hour_g)+"시"+str(min_g)+"분"+str(sec_g)+"초"))
#        self.time_label.setStyleSheet("color:white")
#        self.time_label.setFont(weather_font)


#thunder light
        #board.digital_write(thunder_l,1)

    def next_hour(self):
        global hour_g
        if hour_g==23:
           hour_g=0
        else:
           hour_g=hour_g+1

        if hour_g >= 9 and hour_g <18:
           board.digital_write(day_l,1)
        else:
           board.digital_write(day_l,0)

    def next_min(self):
        global min_g
        if min_g==59:
           min_g=0
           self.next_hour()
        else:
           min_g=min_g+1

    def next_sec(self):
        global sec_g
        if sec_g==59:
           sec_g=0
           self.next_min()
        else:
           sec_g=sec_g+1



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





