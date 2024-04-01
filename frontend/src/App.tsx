import {
  Admin,
  Resource,
  ListGuesser,
  EditGuesser,
  ShowGuesser,
} from "react-admin";
import { dataProvider } from "./dataProvider";
import { restDataProvider } from "./restFrameworkDataProvider";
import { authProvider } from "./authProvider";
import {UserList, UserShow, UserEdit , UserCreate} from "./resources/users";

export const App = () => (
  <Admin dataProvider={restDataProvider} authProvider={authProvider}>
    <Resource
      name="users"
      list={UserList}
      edit={UserEdit}
      create={UserCreate}
      show={UserShow}
    />
  </Admin>
);
