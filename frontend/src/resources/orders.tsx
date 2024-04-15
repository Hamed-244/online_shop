import { List, Datagrid, TextField, EmailField, BooleanField, NumberField, RichTextField} from "react-admin";
import { Show, SimpleShowLayout, DateField} from 'react-admin';
import { Edit,EditButton, SimpleForm, TextInput, PasswordInput, DateInput,DateTimeInput, required, NumberInput, BooleanInput, ArrayInput, SimpleFormIterator } from 'react-admin';
import { Create , Filter, SearchInput,SelectInput, ReferenceInput,ReferenceField, ArrayField, ReferenceManyField,SingleFieldList,ChipField,ReferenceArrayInput,ReferenceArrayField} from 'react-admin';

const OrdersFilter = [
    <SearchInput source="q" alwaysOn />,
    <ReferenceInput source="user" reference="users" label="Filter by user"/>,
    <ReferenceInput source="shipping_address" reference="shipping-addresses" label="Filter by Shipping address"/>,
    <SelectInput source="status" label="Filter by status" choices={[
        { id: 'pending', name: 'Pending' },
        { id: 'delivering', name: 'Delivering' },
        { id: 'canceled', name: 'Canceled' },
    ]} />
];

export const OrdersList = () => (
    <List filters={OrdersFilter}>
        <Datagrid rowClick="show">
            <NumberField source="id" />
            <ReferenceField source="user" reference="users" label="User"/>
            <ReferenceField source="shipping_address" reference="shipping-addresses" label="shipping Address"/>
            <NumberField source="final_price" />
            <TextField source="status" />
            <DateField source="updated_at"/>
        </Datagrid>
    </List>
);


export const OrderShow = () => (
    <Show>
        <SimpleShowLayout>
            <NumberField source="id" />
            <ReferenceField source="user" reference="users" label="User"/>
            <ReferenceField source="shipping_address" reference="shipping-addresses" label="shipping Address"/>
            <NumberField source="final_price" />
            <TextField source="status" />
            <DateField source="order_date"/>
            <DateField source="created_at"/>
            <DateField source="updated_at"/>
        </SimpleShowLayout>
    </Show>
);


export const OrderEdit = () => (
    <Edit>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ReferenceInput source="user" reference="users" label="User"/>
            <ReferenceInput source="shipping_address" reference="shipping-addresses" label="shipping Address"/>
            <NumberInput source="final_price" />
            <SelectInput source="status" choices={[
                { id: 'pending', name: 'Pending' },
                { id: 'delivering', name: 'Delivering' },
                { id: 'canceled', name: 'Canceled' },
            ]} />
            <DateInput source="order_date"/>
            <DateInput source="created_at"/>
            <DateInput source="updated_at"/>
        </SimpleForm>
    </Edit>
);


export const OrderCreate = () => (
    <Create>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ReferenceInput source="user" reference="users" label="User"/>
            <ReferenceInput source="shipping_address" reference="shipping-addresses" label="shipping Address"/>
            <NumberInput disabled source="final_price" />
            <SelectInput source="status" choices={[
                { id: 'pending', name: 'Pending' },
                { id: 'delivering', name: 'Delivering' },
                { id: 'canceled', name: 'Canceled' },
            ]} />
            <DateInput source="order_date"/>
            <DateInput source="created_at"/>
            <DateInput source="updated_at"/>
        </SimpleForm>
    </Create>
);