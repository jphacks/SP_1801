//
//  ViewController0.swift
//  TyokinshiAI_JPHACKS2018
//
//  Created by 中井崚日 on 2018/10/21.
//  Copyright © 2018年 中井崚日. All rights reserved.
//

import UIKit

class ViewController0: UIViewController {
    
    @IBOutlet weak var Image_AI: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        Image_AI.image = UIImage(named:"tyokinAI.png")
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
}
