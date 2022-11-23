import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthService, LoginResponseData } from './auth.service';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
})
export class AuthComponent {
  isLogin = true;
  isLoding = false;
  error = null;

  constructor(private authService: AuthService, private router: Router) {}

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

    let authObs: Observable<LoginResponseData>;

    this.isLoding = true;
    this.authService.signup(email, password).subscribe({
      next: (resData) => {
        this.router.navigate(['']);
        this.isLoding = false;
      },
      error: (errRes) => {
        this.isLoding = false;
        this.error = errRes;
        console.log(errRes);
      },
    });
    form.reset();
  }
}
