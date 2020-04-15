import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  private socket;
  constructor() {
    this.socket = new WebSocket(`ws://localhost:8080/online/`);
  }
}
