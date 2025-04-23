export interface User {
    id: number;
    username: string;
    email: string;
  }
  
  export interface AuthResponse {
    user: User;
    refresh: string;
    access: string;
  }