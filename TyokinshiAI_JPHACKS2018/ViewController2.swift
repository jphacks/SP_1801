//
//  ViewController2.swift
//  TyokinshiAI_JPHACKS2018
//
//  Created by 中井崚日 on 2018/10/20.
//  Copyright © 2018年 中井崚日. All rights reserved.
//

import Foundation
import UIKit

class ViewController2: UIViewController {
    
    @IBOutlet weak var Image_AI: UIImageView!
    @IBOutlet weak var Label_tyokin_team: UILabel!
    @IBOutlet weak var Label_tukaimiti: UILabel!
    @IBOutlet weak var Label_tyokin_personal: UILabel!
    @IBOutlet weak var Label_yutai: UILabel!
    
    public var myStr:Int = 0
    var myStr_save:Int = 0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        Image_AI.image = UIImage(named:"tyokinAI.png")

        Label_tyokin_personal.text = String(myStr)
        myStr_save = myStr
        
        let tyokin_team = myStr+400
        Label_tyokin_team.text = String(tyokin_team)
        
        if tyokin_team >= 0 && tyokin_team < 500{
            Label_tukaimiti.text = "貯金不足"
        }else if tyokin_team >= 500 && tyokin_team < 1000{
            Label_tukaimiti.text = "メキシコ"
        }else if tyokin_team >= 1000 && tyokin_team < 1500{
            Label_tukaimiti.text = "グァマテラ"
        }else if tyokin_team >= 1500 && tyokin_team < 2000{
            Label_tukaimiti.text = "ブルーマウンテン"
        }else if tyokin_team >= 2000 && tyokin_team < 2500{
            Label_tukaimiti.text = "クリスタルマウンテン"
        }else if tyokin_team >= 2500{
            Label_tukaimiti.text = "コスタリカ"
        }
        
        let yutai = myStr/100
        Label_yutai.text = String(yutai)
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    /*数値を別の画面の変数に引き継ぐ*/
    // Segue 準備
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if (segue.identifier == "toViewController3") {
        // SecondViewControllerをインスタンス化
        let mainVc: ViewController3 = (segue.destination as? ViewController3)!
        // 値を渡す
        
        mainVc.vc2_save = Int(myStr_save)
        
        }
    }

    
}
