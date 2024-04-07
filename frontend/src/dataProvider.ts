import drfProvider, { jwtTokenAuthProvider, fetchJsonWithAuthJWTToken } from 'ra-data-django-rest-framework';


export const restDataProvider = drfProvider(import.meta.env.VITE_SIMPLE_REST_URL , fetchJsonWithAuthJWTToken);