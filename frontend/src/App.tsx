import {
  Admin,
  Resource,
  ListGuesser,
  EditGuesser,
  ShowGuesser,
} from "react-admin";
import { restDataProvider } from "./dataProvider";
import { authProvider } from "./authProvider";
import {UserList, UserShow, UserEdit , UserCreate} from "./resources/users";
import {CategoryList, CategoryShow, CategoryEdit, CategoryCreate} from "./resources/categories";
import {ProductsList, ProductShow, ProductEdit,ProductCreate} from "./resources/products";

export const App = () => (
  <Admin dataProvider={restDataProvider} authProvider={authProvider}>
    <Resource name="users" list={UserList} edit={UserEdit} create={UserCreate} show={UserShow} />
    <Resource name="categories" list={CategoryList} edit={CategoryEdit} create={CategoryCreate} show={CategoryShow} recordRepresentation="name"/>
    <Resource name="products" list={ProductsList} edit={ProductEdit} create={ProductCreate} show={ProductShow} />
  </Admin>
);
