import drfProvider, { jwtTokenAuthProvider, fetchJsonWithAuthJWTToken} from 'ra-data-django-rest-framework';
import {
  CreateParams,
  UpdateParams,
  DataProvider,
  fetchUtils,
} from "react-admin";

const baseDataProvider = drfProvider(import.meta.env.VITE_SIMPLE_REST_URL , fetchJsonWithAuthJWTToken);
const endpoint = import.meta.env.VITE_SIMPLE_REST_URL;

type PostParams = {
  id: string;
  product: string;
  image: {
    rawFile: File;
    src?: string;
    title?: string;
  };
};

const createProductImageFormData = (
  params: CreateParams<PostParams> | UpdateParams<PostParams>
) => {
  const formData = new FormData();
  params.data.image?.rawFile && formData.append("image", params.data.image.rawFile);
  params.data.product && formData.append("product", params.data.product);

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

    return baseDataProvider.update(resource, params);
  },
};