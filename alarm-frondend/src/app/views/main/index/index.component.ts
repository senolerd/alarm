import { Component, OnInit } from '@angular/core';
import { CraiglistService, ISalesType } from 'src/app/services/craiglist.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.scss']
})
export class IndexComponent implements OnInit {

  constructor(
    private _craiglistSvc: CraiglistService
  ) { }

  sales_types:ISalesType[] = []

  ngOnInit(): void {
    this._craiglistSvc.get_sales_types().subscribe(sales_types =>{
      this.sales_types = sales_types
    })
  }

}
