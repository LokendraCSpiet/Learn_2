import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Item{
  id: number;
  name: string;
}

@Injectable({
  providedIn: 'root'
})
export class ItemService {
  private apiUrl = 'http://127.0.0.1:5000/items';

  constructor(private http: HttpClient) {}

  getItems(): Observable<Item[]> {
    return this.http.get<Item[]>(this.apiUrl);
  }

  getItem(itemId: number): Observable<Item> {
    return this.http.get<Item>(`${this.apiUrl}/$(itemId)`);
  }

  createItem(name: string): Observable<Item> {
    return this.http.post<Item>(this.apiUrl, { name });
  }

  updateItem(itemId: number, name: string): Observable<Item> {
    return this.http.put<Item>(`${this.apiUrl}/${itemId}`, { name });
  }

  deleteItem(itemId: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${itemId}`);
  }
}
