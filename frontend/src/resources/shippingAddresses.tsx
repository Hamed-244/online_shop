import { List, Datagrid, TextField, EmailField, BooleanField, NumberField, RichTextField} from "react-admin";
import { Show, SimpleShowLayout, DateField} from 'react-admin';
import { Edit,EditButton, SimpleForm, TextInput, PasswordInput, DateInput,DateTimeInput, required, NumberInput, BooleanInput, ArrayInput, SimpleFormIterator } from 'react-admin';
import { Create , Filter, SearchInput,SelectInput, ReferenceInput,ReferenceField, ArrayField, ReferenceManyField,SingleFieldList,ChipField,ReferenceArrayInput,ReferenceArrayField} from 'react-admin';

const shippingAddressesFilter = [
    <SearchInput source="q" alwaysOn />,
    <ReferenceInput label="Filter by user" source="user" reference="users" />,
    <TextInput label="Filter by city" source="city" />,
    <TextInput label="Filter by state" source="state" />,
    <TextInput label="Filter by postal_code" source="postal_code" />,
];

export const ShippingAddressesList = () => (
    <List filters={shippingAddressesFilter}>
        <Datagrid rowClick="show">
            <NumberField source="id" />
            <ReferenceField source="user" reference="users"></ReferenceField>
            <TextField source="title" />
            <TextField source="address_line1" />
            <TextField source="address_line2" />
            <TextField source="city" />
            <TextField source="state" />
            <TextField source="postal_code" />
        </Datagrid>
    </List>
);


export const ShippingAddressShow = () => (
    <Show>
        <SimpleShowLayout>
            <NumberField source="id" />
            <ReferenceField source="user" reference="users"></ReferenceField>
            <TextField source="title" />
            <TextField source="address_line1" />
            <TextField source="address_line2" />
            <TextField source="city" />
            <TextField source="state" />
            <TextField source="postal_code" />
        </SimpleShowLayout>
    </Show>
);


export const ShippingAddressEdit = () => (
    <Edit>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ReferenceInput source="user" reference="users"></ReferenceInput>
            <TextInput source="title" />
            <TextInput source="address_line1" />
            <TextInput source="address_line2" />
            <TextInput source="city" />
            <TextInput source="state" />
            <TextInput source="postal_code" />
        </SimpleForm>
    </Edit>
);


export const ShippingAddressCreate = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="user" reference="users"></ReferenceInput>
            <TextInput source="title" />
            <TextInput source="address_line1" />
            <TextInput source="address_line2" />
            <TextInput source="city" />
            <TextInput source="state" />
            <TextInput source="postal_code" />
        </SimpleForm>
    </Create>
);