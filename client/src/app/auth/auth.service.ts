import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';

export interface AuthResponseData {
  message: string;
}

export interface LoginResponseData {
  access: string;
  refresh:string
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  constructor(private http: HttpClient) {}

  signup(email: string, password: string) {
    return this.http
      .post<AuthResponseData>('http://127.0.0.1:8000/api/account/createuser/', {
        email: email,
        password: password,
      })
      .pipe(
        catchError((errorRes: any) => {
          let errorMessage = 'An Unknow Error occurred';
          if (!errorRes.error || !errorRes.error.error) {
            return throwError(() => new Error(errorMessage));
          }
          switch (errorRes.error.error.message) {
            case 'User with Email Already Exits':
              errorMessage = 'User with Email Already Exits';
          }
          return throwError(() => new Error(errorMessage));
        })
      );
  }

  login(email: string, password: string) {
    return this.http.post<LoginResponseData>(
      'http://127.0.0.1:8000/api/account/login/token/',
      {
        email: email,
        password: password,
      }
    );
  }
}
