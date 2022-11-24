import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthService, LoginResponseData, AuthResponseData } from './auth.service';
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

  constructor(private authService: AuthService, private router: Router) { }

  onSwitch() {
    this.isLogin = !this.isLogin;
  }

  onSubmit(form: NgForm) {
    if (!form.valid) {
      return;
    }
    const email = form.value.email;
    const password = form.value.password;

    this.isLoding = true;

    if (this.isLogin) {
      let authObs: Observable<LoginResponseData>
      authObs = this.authService.login(email, password);
      authObs.subscribe({
        next: (resData) => {
          this.isLoding = false;
          localStorage.setItem('accessToken', resData.access);
          localStorage.setItem('refreshToken', resData.refresh);
          this.router.navigate(['/home']);
        },
        error: (errRes) => {
          this.isLoding = false;
          this.error = errRes;
        },
      });
    } else {
      let authObs: Observable<AuthResponseData>
      authObs = this.authService.signup(email, password);
      authObs.subscribe({
        next: (resData) => {
          console.log(resData);
          this.isLoding = false;
        },
        error: (errRes) => {
          this.isLoding = false;
          this.error = errRes;
        },
      });
    }


    form.reset();
  }
}
