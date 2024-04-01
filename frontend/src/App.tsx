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

export const App = () => (
  <Admin dataProvider={restDataProvider} authProvider={authProvider}>
    <Resource
      name="users"
      list={ListGuesser}
      edit={EditGuesser}
      show={ShowGuesser}
    />
  </Admin>
);
