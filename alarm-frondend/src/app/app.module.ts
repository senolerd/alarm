import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from './app.component';
import { MatSidenavModule} from '@angular/material/sidenav'; 
import { MatSelectModule } from '@angular/material/select'; 
import {MatButtonModule} from '@angular/material/button'; 
import {MatIconModule} from '@angular/material/icon';
import { HeaderComponent } from './views/header/header.component';
import { MainComponent } from './views/main/main.component';
import { FooterComponent } from './views/footer/footer.component';
import { IndexComponent } from './views/main/index/index.component';
import { LoginComponent } from './views/main/login/login.component';
import { RegisterComponent } from './views/main/register/register.component';
import { AboutComponent } from './views/main/about/about.component';
import {HttpClientModule} from '@angular/common/http'



@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    MainComponent,
    FooterComponent,
    IndexComponent,
    LoginComponent,
    RegisterComponent,
    AboutComponent,

  ],
  imports: [
    BrowserModule,
    MatSidenavModule,
    MatSelectModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatIconModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
