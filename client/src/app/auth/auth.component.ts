import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
})
export class AuthComponent {
  isLogin = true;

  constructor(private authService: AuthService) {}

  onSwitch() {
    this.isLogin = !this.isLogin;
  }
  onSubmit(form: NgForm) {
    if (!form.valid) {
      return;
    }
    console.log(form.value);
    const email = form.value.email;
    const password = form.value.password;
    this.authService.signup(email, password).subscribe({
      next: (resData) => {
        console.log(resData);
      },
      error: (error) => {
        console.log(error);
      },
    });
    form.reset();
  }
}
