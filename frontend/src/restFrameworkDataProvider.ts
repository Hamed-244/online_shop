import drfProvider from 'ra-data-django-rest-framework';

export const restDataProvider = drfProvider(import.meta.env.VITE_SIMPLE_REST_URL);