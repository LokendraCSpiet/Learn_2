import { Component } from '@angular/core'; 
import { RouterOutlet } from '@angular/router';
import { ItemListComponent } from './item-list/item-list.component'; 
import { ItemService } from './item.service';
import { HttpClientModule } from '@angular/common/http';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,ItemListComponent, HttpClientModule],
  providers: [ItemService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'taskApp';
}