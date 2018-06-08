/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.7.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTableView>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QTableView *tab_botnet;
    QPushButton *btn_botnet_none;
    QPushButton *btn_botnet_all;
    QSlider *slider_synflood;
    QSlider *slider_httpflood;
    QSlider *slider_slowloris;
    QPushButton *btn_set;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QTextBrowser *textBrowser;
    QPushButton *btn_status;
    QPushButton *btn_botnet_load;
    QLineEdit *lineEdit;
    QRadioButton *radioButton;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(800, 600);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        tab_botnet = new QTableView(centralWidget);
        tab_botnet->setObjectName(QStringLiteral("tab_botnet"));
        tab_botnet->setGeometry(QRect(20, 60, 401, 480));
        btn_botnet_none = new QPushButton(centralWidget);
        btn_botnet_none->setObjectName(QStringLiteral("btn_botnet_none"));
        btn_botnet_none->setGeometry(QRect(360, 10, 60, 40));
        QFont font;
        font.setFamily(QStringLiteral("Georgia"));
        font.setPointSize(10);
        btn_botnet_none->setFont(font);
        btn_botnet_all = new QPushButton(centralWidget);
        btn_botnet_all->setObjectName(QStringLiteral("btn_botnet_all"));
        btn_botnet_all->setGeometry(QRect(280, 10, 60, 40));
        btn_botnet_all->setFont(font);
        slider_synflood = new QSlider(centralWidget);
        slider_synflood->setObjectName(QStringLiteral("slider_synflood"));
        slider_synflood->setGeometry(QRect(500, 50, 20, 200));
        slider_synflood->setOrientation(Qt::Vertical);
        slider_httpflood = new QSlider(centralWidget);
        slider_httpflood->setObjectName(QStringLiteral("slider_httpflood"));
        slider_httpflood->setGeometry(QRect(620, 50, 20, 200));
        slider_httpflood->setOrientation(Qt::Vertical);
        slider_slowloris = new QSlider(centralWidget);
        slider_slowloris->setObjectName(QStringLiteral("slider_slowloris"));
        slider_slowloris->setGeometry(QRect(740, 50, 20, 200));
        slider_slowloris->setOrientation(Qt::Vertical);
        btn_set = new QPushButton(centralWidget);
        btn_set->setObjectName(QStringLiteral("btn_set"));
        btn_set->setGeometry(QRect(670, 270, 100, 40));
        QFont font1;
        font1.setFamily(QStringLiteral("Georgia"));
        font1.setPointSize(12);
        btn_set->setFont(font1);
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(420, 10, 120, 20));
        label->setFont(font);
        label->setAlignment(Qt::AlignCenter);
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(540, 10, 120, 20));
        label_2->setFont(font);
        label_2->setAlignment(Qt::AlignCenter);
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(660, 10, 120, 20));
        label_3->setFont(font);
        label_3->setAlignment(Qt::AlignCenter);
        label_4 = new QLabel(centralWidget);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(450, 230, 40, 20));
        QFont font2;
        font2.setFamily(QStringLiteral("Georgia"));
        label_4->setFont(font2);
        label_4->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(450, 50, 40, 20));
        label_5->setFont(font2);
        label_5->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_6 = new QLabel(centralWidget);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(570, 230, 40, 20));
        label_6->setFont(font2);
        label_6->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_7 = new QLabel(centralWidget);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setGeometry(QRect(570, 50, 40, 20));
        label_7->setFont(font2);
        label_7->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_8 = new QLabel(centralWidget);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(690, 230, 40, 20));
        label_8->setFont(font2);
        label_8->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        label_9 = new QLabel(centralWidget);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setGeometry(QRect(690, 50, 40, 20));
        label_9->setFont(font2);
        label_9->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);
        textBrowser = new QTextBrowser(centralWidget);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));
        textBrowser->setGeometry(QRect(470, 360, 301, 121));
        btn_status = new QPushButton(centralWidget);
        btn_status->setObjectName(QStringLiteral("btn_status"));
        btn_status->setGeometry(QRect(670, 500, 100, 40));
        btn_status->setFont(font1);
        btn_botnet_load = new QPushButton(centralWidget);
        btn_botnet_load->setObjectName(QStringLiteral("btn_botnet_load"));
        btn_botnet_load->setGeometry(QRect(200, 10, 60, 40));
        btn_botnet_load->setFont(font);
        lineEdit = new QLineEdit(centralWidget);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setGeometry(QRect(20, 10, 160, 40));
        radioButton = new QRadioButton(centralWidget);
        radioButton->setObjectName(QStringLiteral("radioButton"));
        radioButton->setGeometry(QRect(430, 260, 69, 15));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 800, 17));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", Q_NULLPTR));
        btn_botnet_none->setText(QApplication::translate("MainWindow", "None", Q_NULLPTR));
        btn_botnet_all->setText(QApplication::translate("MainWindow", "All", Q_NULLPTR));
        btn_set->setText(QApplication::translate("MainWindow", "Set", Q_NULLPTR));
        label->setText(QApplication::translate("MainWindow", "SYNFlood", Q_NULLPTR));
        label_2->setText(QApplication::translate("MainWindow", "HTTPFlood", Q_NULLPTR));
        label_3->setText(QApplication::translate("MainWindow", "Slowloris", Q_NULLPTR));
        label_4->setText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        label_5->setText(QApplication::translate("MainWindow", "1000", Q_NULLPTR));
        label_6->setText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        label_7->setText(QApplication::translate("MainWindow", "300", Q_NULLPTR));
        label_8->setText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        label_9->setText(QApplication::translate("MainWindow", "300", Q_NULLPTR));
        btn_status->setText(QApplication::translate("MainWindow", "Status", Q_NULLPTR));
        btn_botnet_load->setText(QApplication::translate("MainWindow", "Load", Q_NULLPTR));
        radioButton->setText(QApplication::translate("MainWindow", "RadioButton", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
