//
//  ViewController3.swift
//  TyokinshiAI_JPHACKS2018
//
//  Created by 中井崚日 on 2018/10/20.
//  Copyright © 2018年 中井崚日. All rights reserved.
//

import Foundation
import UIKit

class ViewController3: UIViewController, UIPickerViewDelegate, UIPickerViewDataSource {
    
    @IBOutlet weak var pickerView: UIPickerView!
    @IBOutlet weak var Label_tyokingaku: UILabel!
    
    var vc2_save = 0
    
    // 選択肢
    let dataList = ["0", "50", "100", "200", "300", "400", "500"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Delegate設定
        pickerView.delegate = self
        pickerView.dataSource = self
        
    }
    
    // UIPickerViewの列の数
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    // UIPickerViewの行数、リストの数
    func pickerView(_ pickerView: UIPickerView,
                    numberOfRowsInComponent component: Int) -> Int {
        return dataList.count
    }
    
    // UIPickerViewの最初の表示
    func pickerView(_ pickerView: UIPickerView,
                    titleForRow row: Int,
                    forComponent component: Int) -> String? {
        return dataList[row]
    }
    
    var picker_value_save = ""
    
    // UIPickerViewのRowが選択された時の挙動
    func pickerView(_ pickerView: UIPickerView,
                    didSelectRow row: Int,
                    inComponent component: Int) {
        print(dataList[row])
        Label_tyokingaku.text = dataList[row]
        
        picker_value_save = dataList[row]

    }
    
    
    /*数値を別の画面の変数に引き継ぐ*/
    // Segue 準備
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        //if (segue.identifier == "undoViewController2.1") {
            // SecondViewControllerをインスタンス化
            let mainVc: ViewController2 = (segue.destination as? ViewController2)!
            // 値を渡す
        
            mainVc.myStr = Int(picker_value_save)! + vc2_save
            
        //}
    }
    
}
