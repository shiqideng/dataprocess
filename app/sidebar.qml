import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 200
    height: 400

    Column {
        anchors.fill: parent
        spacing:

        Button {
            text: "Home"
            onClicked: sidebarClicked("home")
        }
        Button {
            text: "Settings"
            onClicked: sidebarClicked("settings")
        }
        // ... 其他按钮
    }

    // 定义发射信号的函数
    function sidebarClicked(itemName) {
        sidebarClicked(itemName)
    }

    // 定义可以被Python连接的信号
    signal sidebarClicked(string itemName)
}