import { List, Datagrid, TextField, EmailField, BooleanField, NumberField} from "react-admin";
import { Show, SimpleShowLayout, DateField,} from 'react-admin';
import { Edit, SimpleForm, TextInput, PasswordInput, DateInput, required, NumberInput, BooleanInput, ArrayInput, SimpleFormIterator } from 'react-admin';
import { Create , Filter} from 'react-admin';

const UserFilter = () => (
    <Filter>
        <TextInput label="Search by Username" source="username" alwaysOn />
        <BooleanInput label="Is Staff?" source="is_staff" />
        <BooleanInput label="Is Active?" source="is_active" />
        <TextInput label="Search by First Name" source="first_name" />
        <TextInput label="Search by Last Name" source="last_name" />
        <TextInput label="Search by Email" source="email" />
    </Filter>
);

export const UserList = () => (
    <List filters={UserFilter()}>
        <Datagrid rowClick="edit">
            <NumberField source="id" />
            <TextField source="username" />
            <TextField source="first_name" />
            <TextField source="last_name" />
            <EmailField source="email" />
            <BooleanField source="is_staff" />
            <BooleanField source="is_active" />
        </Datagrid>
    </List>
);


export const UserShow = () => (
    <Show>
        <SimpleShowLayout>
            <TextField source="id" />
            <TextField source="username" />
            <TextField source="first_name" />
            <TextField source="last_name" />
            <TextField source="email" />
            <DateField source="last_login" />
            <DateField source="date_joined" />
            <BooleanField source="is_superuser" />
            <BooleanField source="is_staff" />
            <BooleanField source="is_active" />
        </SimpleShowLayout>
    </Show>
);


export const UserEdit = () => (
    <Edit>
        <SimpleForm>
            <NumberInput disabled label="Id" source="id" />
            <PasswordInput label="Password" source="password" />
            <TextInput label="Username" source="username" validate={required()} />
            <TextInput label="First Name" source="first_name" validate={required()} />
            <TextInput label="Last Name" source="last_name" validate={required()} />
            <TextInput label="Email" source="email" />
            <DateInput disabled label="Last login" source="last_login" />
            <DateInput disabled label="Date Joined" source="date_joined" />
            <BooleanInput label="Superuser" source="is_superuser" />
            <BooleanInput label="Staff" source="is_staff" />
            <BooleanInput label="Active" source="is_active" />
        </SimpleForm>
    </Edit>
);


export const UserCreate = () => (
    <Create >
        <SimpleForm>
            <TextInput label="Username" source="username" validate={required()} />
            <PasswordInput label="Password" source="password" validate={required()} />
            <TextInput label="First Name" source="first_name" validate={required()} />
            <TextInput label="Last Name" source="last_name" validate={required()} />
            <TextInput label="Email" source="email" validate={required()} />
            <BooleanInput label="Superuser" source="is_superuser" />
            <BooleanInput label="Staff" source="is_staff" />
            <BooleanInput label="Active" source="is_active" />
        </SimpleForm>
    </Create>
);
