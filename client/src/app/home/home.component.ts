import { Component } from '@angular/core';
import { Project } from './project.model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
})
export class HomeComponent {
  project: Project[] = [
    new Project(
      'Testtitle',
      'Testdescription',
      'https://images.unsplash.com/photo-1610337673044-720471f83677?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1072&q=80'
    ),
  ];
  constructor() {}
  ngOnInit() {}
}
