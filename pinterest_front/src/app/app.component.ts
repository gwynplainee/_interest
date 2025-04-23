import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { PinboardComponent } from "./components/pinboard/pinboard.component";
import { MatIconModule } from '@angular/material/icon';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { TopbarComponent } from "./components/topbar/topbar.component"; 


@Component({
  selector: 'app-root',
  imports: [PinboardComponent, MatIconModule, SidebarComponent, RouterModule, TopbarComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'pinterest_front';
}
export class AppModule {}
