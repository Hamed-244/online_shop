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


type ProductParams = {
  id: string;
  product: string;
  image: {
    rawFile: File;
    src?: string;
    title?: string;
  };
  name: string;
  slug: string;
  description: string;
  price: string;
  amount: string;
  category: string;
};

const createProductFormData = (
  params: CreateParams<ProductParams> | UpdateParams<ProductParams>
) => {
  const formData = new FormData();
  params.data.image?.rawFile && formData.append("image", params.data.image.rawFile);
  params.data.product && formData.append("product", params.data.product);
  params.data.name && formData.append("name", params.data.name);
  params.data.slug && formData.append("slug", params.data.slug);
  params.data.description && formData.append("description", params.data.description);
  params.data.amount && formData.append("amount", params.data.amount);
  params.data.price && formData.append("price", params.data.price);
  params.data.category && formData.append("category", params.data.category);

  return formData;
};

type CategoryParams = {
  id: string;
  image: {
    rawFile: File;
    src?: string;
    title?: string;
  };
  name: string;
  slug: string;
  description: string;
  updated_at: string;
  created_at: string;
  parent_category: string;
};

const createCategoryFormData = (
  params: CreateParams<CategoryParams> | UpdateParams<CategoryParams>
) => {
  const formData = new FormData();
  params.data.image?.rawFile && formData.append("image", params.data.image.rawFile);
  params.data.name && formData.append("name", params.data.name);
  params.data.slug && formData.append("slug", params.data.slug);
  params.data.description && formData.append("description", params.data.description);
  params.data.updated_at && formData.append("updated_at", params.data.updated_at);
  params.data.parent_category && formData.append("parent_category", params.data.parent_category);
  params.data.created_at && formData.append("created_at", params.data.created_at);

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
    else if (resource === "products") {
      const formData = createProductFormData(params);
      return fetchUtils
        .fetchJson(`${endpoint}/${resource}/`, {
          method: "POST",
          body: formData,
          headers: getHeaders()
        })
        .then(({ json }) => ({ data: json }));
    }
    else if (resource === "categories") {
      const formData = createCategoryFormData(params);
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
    else if (resource === "products") {
      const formData = createProductFormData(params);
      return fetchUtils
        .fetchJson(`${endpoint}/${resource}/${params.id}/`, {
          method: "PUT",
          body: formData,
          headers: getHeaders()
        })
        .then(({ json }) => ({ data: json }));
    }
    else if (resource === "categories") {
      const formData = createCategoryFormData(params);
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