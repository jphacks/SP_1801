//
//  ViewController0.swift
//  TyokinshiAI_JPHACKS2018
//
//  Created by 中井崚日 on 2018/10/20.
//  Copyright © 2018年 中井崚日. All rights reserved.
//

import Foundation
import UIKit

class ViewController0: UIViewController {
    
    @IBOutlet weak var Image_AI2: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        Image_AI2.image = UIImage(named:"tyokinAI.png")
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
}
