import { Routes } from '@angular/router';
import { PinboardComponent } from './components/pinboard/pinboard.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';

export const routes: Routes = [
    {path: '', component:PinboardComponent},
    {path: 'login', component: LoginComponent},
    {path: 'register', component: RegisterComponent}
];
