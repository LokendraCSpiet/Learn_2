import { Routes } from '@angular/router';
import { OrderComponent } from './order/order.component';
import { HomeComponent } from './home/home.component';


export const routes: Routes = [
    { path:"", pathMatch:"full", redirectTo:"/home"},
    { path:"home", component: HomeComponent},
    { path: 'order', component: OrderComponent}
];
