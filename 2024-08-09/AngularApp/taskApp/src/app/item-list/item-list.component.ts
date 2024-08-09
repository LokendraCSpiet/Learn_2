import { Component, OnInit } from '@angular/core';
import { ItemService } from '../item.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

interface Item { 
  id: number;
  name: string;
}

@Component({
  selector: 'app-item-list',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './item-list.component.html',
  styleUrl: './item-list.component.css'
})
export class ItemListComponent implements OnInit {
  items: Item[] = [];
  newItemName: string = '';

  constructor(private itemService: ItemService){}
  
  ngOnInit(): void {
    this.loadItems();
  }

  loadItems(): void {
    this.itemService.getItems().subscribe((items) => {
      this.items = items;
    });
  }

  addItem(): void {
    if (this.newItemName) {
      this.itemService.createItem(this.newItemName).subscribe((item) => {
        this.items.push(item);
        this.newItemName = '';  // Clear input field

      })
    }
  }

  deleteItem(itemId: number): void {
    this.itemService.deleteItem(itemId).subscribe(() => {
      this.items = this.items.filter((item) => item.id !== itemId);
    });
  }




}

