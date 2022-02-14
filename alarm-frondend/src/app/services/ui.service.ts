import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

export interface ImenuItem {
  name:String, status:Boolean
}

@Injectable({
  providedIn: 'root',
})
export class UiService {
  constructor() {
  }


  menu_list:ImenuItem[] = [
    { name: 'Home', status: true },
    { name: 'Login', status: false },
    { name: 'Register', status: false },
    { name: 'About', status: false },
  ];

  update_menu_item_status(item_name:String="Home"){
    for (let menu_item of this.menu_list){
      menu_item.name === item_name ? menu_item.status = true : menu_item.status = false
    }
    this.menuBS.next(this.menu_list)
    this.active_menu_itemBS.next(item_name)
  }
  
  toggleMenu(){
    this.menu_openBS.next(!this.menu_openBS.value)
  }

  menuBS = new BehaviorSubject<ImenuItem[]>(this.menu_list);
  active_menu_itemBS = new BehaviorSubject<String>("");
  menu_openBS = new BehaviorSubject(false)
  widthBS = new BehaviorSubject<number>(window.innerWidth)

}
