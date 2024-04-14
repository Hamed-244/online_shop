import drfProvider, { jwtTokenAuthProvider, fetchJsonWithAuthJWTToken} from 'ra-data-django-rest-framework';
import {
  CreateParams,
  UpdateParams,
  DataProvider,
  fetchUtils,
} from "react-admin";

const baseDataProvider = drfProvider(import.meta.env.VITE_REST_URL , fetchJsonWithAuthJWTToken);
const endpoint = import.meta.env.VITE_REST_URL;

type ProductImagesParams = {
  id: string;
  product: string;
  image: {
    rawFile: File;
    src?: string;
    title?: string;
  };
};

const createProductImageFormData = (
  params: CreateParams<ProductImagesParams> | UpdateParams<ProductImagesParams>
) => {
  const formData = new FormData();
  params.data.image?.rawFile && formData.append("image", params.data.image.rawFile);
  params.data.product && formData.append("product", params.data.product);

  return formData;
};

type UserParams = {
  id: string;
  username: string;
  first_name: string;
  last_name: string;
  email: string;
  is_superuser: boolean;
  is_staff: boolean;
  is_active: boolean;
  profile_image: {
    rawFile: File;
    src?: string;
    title?: string;
  };
};

const createUserFormData = (
  params: CreateParams<UserParams> | UpdateParams<UserParams>
) => {
  const formData = new FormData();
  params.data.profile_image?.rawFile && formData.append("profile_image", params.data.profile_image.rawFile);
  formData.append("username", params.data.username);
  formData.append("password", params.data.password);
  formData.append("first_name", params.data.first_name);
  formData.append("last_name", params.data.last_name);
  formData.append("email", params.data.email);
  formData.append("is_superuser", params.data.is_superuser ? "true" : "false");
  formData.append("is_staff", params.data.is_staff ? "true" : "false");
  formData.append("is_active", params.data.is_active ? "true" : "false");

  return formData;
};

const getHeaders = () => {
  const token = localStorage.getItem('access');
  console.log(token)
  return new Headers({
    'Authorization': `Bearer ${token}`,
  });
};

export const dataProvider: DataProvider = {
  ...baseDataProvider,
  create: (resource, params) => {
    if (resource === "product-images") {
      const formData = createProductImageFormData(params);
      return fetchUtils
        .fetchJson(`${endpoint}/${resource}/`, {
          method: "POST",
          body: formData,
          headers: getHeaders()
        })
        .then(({ json }) => ({ data: json }));
    }
    else if (resource === "users") {
      const formData = createUserFormData(params);
      return fetchUtils
        .fetchJson(`${endpoint}/${resource}/`, {
          method: "POST",
          body: formData,
          headers: getHeaders()
        })
        .then(({ json }) => ({ data: json }));
    }

    return baseDataProvider.create(resource, params);
  },
  update: (resource, params) => {
    if (resource === "product-images") {
      const formData = createProductImageFormData(params);
      formData.append("id", params.id);
      return fetchUtils
        .fetchJson(`${endpoint}/${resource}/${params.id}/`, {
          method: "PUT",
          body: formData,
          headers: getHeaders()
        })
        .then(({ json }) => ({ data: json }));
    }
    else if (resource === "users") {
      const formData = createUserFormData(params);
      return fetchUtils
        .fetchJson(`${endpoint}/${resource}/${params.id}/`, {
          method: "PUT",
          body: formData,
          headers: getHeaders()
        })
        .then(({ json }) => ({ data: json }));
    }
    return baseDataProvider.update(resource, params);
  },
};