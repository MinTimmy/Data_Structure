#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "string"
#include "random"
#include "QLabel"
#include <iostream>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_pushButton_clicked()
{
    QString str= ui->lineEdit->text();

    this->amount = str.toInt();

    this->num = new int[this->amount];

    for (int i = 1; i < this->amount ;i++ ) {
        num[i] = rand();
    }

    QLabel *label;
    label = new QLabel(this);

    QString s[this->amount];
    QString S;
    for(int i = 0; i < this->amount; i++){
        s[i] = QString::number(num[i]);
        label->setGeometry(QRect(QPoint(1,0+(i+1)*2),QSize(1, 1)));
        label->setText("s[i]");
        label->show();

        S = s[i] + " ";
    }

    label->clear();
    //label->setText("fsdfds");
    label->show();


}
