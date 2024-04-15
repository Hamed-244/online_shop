import { List, Datagrid, TextField, EmailField, BooleanField, NumberField, RichTextField} from "react-admin";
import { Show, SimpleShowLayout, DateField} from 'react-admin';
import { Edit,EditButton, SimpleForm, TextInput, PasswordInput, DateInput,DateTimeInput, required, NumberInput, BooleanInput, ArrayInput, SimpleFormIterator } from 'react-admin';
import { Create , Filter, SearchInput,SelectInput, ReferenceInput,ReferenceField, ArrayField, ReferenceManyField,SingleFieldList,ChipField,ReferenceArrayInput,ReferenceArrayField} from 'react-admin';

const OrderItemssFilter = [
    <SearchInput source="q" alwaysOn />,
    <ReferenceInput source="order" reference="orders" label="Filter by Order"/>,
    <ReferenceInput source="product" reference="products" label="Filter by Product"/>,
    <NumberInput source="quantity" label="Filter by quantity"/>
];

export const OrderItemsList = () => (
    <List filters={OrderItemssFilter}>
        <Datagrid rowClick="show">
            <NumberField source="id" />
            <ReferenceField source="order" reference="orders" label="Order"/>
            <ReferenceField source="product" reference="products" label="Product"/>
            <NumberField source="quantity" />
            <NumberField source="total_price" />
            <NumberField source="purchase_price" />
            <DateField source="created_at"/>
        </Datagrid>
    </List>
);


export const OrderItemShow = () => (
    <Show>
        <SimpleShowLayout>
            <NumberField source="id" />
            <ReferenceField source="order" reference="orders" label="Order"/>
            <ReferenceField source="product" reference="products" label="Product"/>
            <NumberField source="quantity" />
            <NumberField source="total_price" />
            <NumberField source="purchase_price" />
            <DateField source="created_at"/>
        </SimpleShowLayout>
    </Show>
);


export const OrderItemEdit = () => (
    <Edit>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ReferenceInput source="order" reference="orders" label="Order"/>
            <ReferenceInput source="product" reference="products" label="Product"/>
            <NumberInput source="quantity" />
            <NumberInput source="total_price" />
            <NumberInput source="purchase_price" />
            <DateInput source="created_at"/>
        </SimpleForm>
    </Edit>
);


export const OrderItemCreate = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="order" reference="orders" label="Order"/>
            <ReferenceInput source="product" reference="products" label="Product"/>
            <NumberInput source="quantity" />
            <NumberInput disabled source="total_price" />
            <NumberInput disabled source="purchase_price" />
            <DateInput source="created_at"/>
        </SimpleForm>
    </Create>
);