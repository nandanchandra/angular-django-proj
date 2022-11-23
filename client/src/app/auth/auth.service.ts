import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface AuthResponseData {
  message: string;
}

@Injectable({ providedIn: 'root' })
export class AuthService {
  constructor(private http: HttpClient) {}

  signup(email: string, password: string) {
    return this.http.post<AuthResponseData>(
      'http://127.0.0.1:8000/api/account/createuser/',
      {
        email: email,
        password: password,
      }
    );
  }
}
