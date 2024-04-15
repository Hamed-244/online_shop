import drfProvider, { tokenAuthProvider, fetchJsonWithAuthToken, jwtTokenAuthProvider, fetchJsonWithAuthJWTToken } from 'ra-data-django-rest-framework';

export const authProvider = jwtTokenAuthProvider({obtainAuthTokenUrl: import.meta.env.VITE_AUTHENTICATION_URL});