import {
  Admin,
  Resource,
  ListGuesser,
  EditGuesser,
  ShowGuesser,
} from "react-admin";
import { dataProvider } from "./dataProvider";
import { authProvider } from "./authProvider";
import {UserList, UserShow, UserEdit , UserCreate} from "./resources/users";
import {CategoryList, CategoryShow, CategoryEdit, CategoryCreate} from "./resources/categories";
import {ProductsList, ProductShow, ProductEdit,ProductCreate} from "./resources/products";
import { ProductImageList ,ProductImageShow, ProductImageEdit, ProductImageCreate} from "./resources/productImages";
import { ShippingAddressesList,ShippingAddressShow ,ShippingAddressEdit,ShippingAddressCreate} from "./resources/shippingAddresses";
import { OrdersList,OrderCreate,OrderEdit,OrderShow } from "./resources/orders";
import { OrderItemsList,OrderItemCreate,OrderItemEdit,OrderItemShow } from "./resources/orderItems";
import { PaymentsList, PaymentShow,PaymentEdit,PaymentCreate } from "./resources/payments";

export const App = () => (
  <Admin dataProvider={dataProvider} authProvider={authProvider}>
    <Resource name="users" list={UserList} edit={UserEdit} create={UserCreate} show={UserShow} recordRepresentation="username"/>
    <Resource name="categories" list={CategoryList} edit={CategoryEdit} create={CategoryCreate} show={CategoryShow} recordRepresentation="name"/>
    <Resource name="products" list={ProductsList} edit={ProductEdit} create={ProductCreate} show={ProductShow} recordRepresentation="name"/>
    <Resource name="product-images" list={ProductImageList} edit={ProductImageEdit} create={ProductImageCreate} show={ProductImageShow} />
    <Resource name="shipping-addresses" list={ShippingAddressesList} create={ShippingAddressCreate} edit={ShippingAddressEdit} show={ShippingAddressShow} recordRepresentation="title"/>
    <Resource name="orders" list={OrdersList} create={OrderCreate} edit={OrderEdit} show={OrderShow} recordRepresentation="id"/>
    <Resource name="order-items" list={OrderItemsList} create={OrderItemCreate} edit={OrderItemEdit} show={OrderItemShow} />
    <Resource name="payments" list={PaymentsList} create={PaymentCreate} edit={PaymentEdit} show={PaymentShow} />
  </Admin>
);
