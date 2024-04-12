import { List, Datagrid, TextField, EmailField, BooleanField, NumberField, RichTextField} from "react-admin";
import { Show, SimpleShowLayout, DateField} from 'react-admin';
import { Edit,EditButton, SimpleForm, TextInput, PasswordInput, DateInput,DateTimeInput, required, NumberInput, BooleanInput, ArrayInput, SimpleFormIterator } from 'react-admin';
import { Create , Filter, SearchInput,SelectInput, ReferenceInput,ReferenceField, ArrayField, ReferenceManyField,SingleFieldList,ChipField,ReferenceArrayInput,ReferenceArrayField} from 'react-admin';

const PaymentsFilter = [
    <SearchInput source="q" alwaysOn />,
    <ReferenceInput source="order" reference="orders" label="Filter by Order"/>,
    <SelectInput source="status" label="Filter by Status" choices={[
        { id: 'done', name: 'Done' },
        { id: 'failed', name: 'Failed' },
        { id: 'refunded', name: 'Refunded' },
    ]} />,
    <SelectInput source="payment_method" label="Filter by Payment Method" choices={[
        { id: 'paypal', name: 'PayPal' },
        { id: 'zarinpal', name: 'ZarinPal' },
    ]} />,
];

export const PaymentsList = () => (
    <List filters={PaymentsFilter}>
        <Datagrid rowClick="show">
            <NumberField source="id" />
            <ReferenceField source="order" reference="orders" label="Order"/>
            <NumberField source="amount" />
            <TextField source="status" />
            <TextField source="payment_method" />
            <DateField source="payment_date"/>
            <DateField source="updated_at"/>
        </Datagrid>
    </List>
);


export const PaymentShow = () => (
    <Show>
        <SimpleShowLayout>
            <NumberField source="id" />
            <ReferenceField source="order" reference="orders" label="Order"/>
            <NumberField source="amount" />
            <TextField source="status" />
            <TextField source="payment_method" />
            <DateField source="payment_date"/>
            <DateField source="updated_at"/>
        </SimpleShowLayout>
    </Show>
);


export const PaymentEdit = () => (
    <Edit>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ReferenceInput source="order" reference="orders" label="Order"/>
            <NumberInput source="amount" />
            <SelectInput source="status" choices={[
                { id: 'done', name: 'Done' },
                { id: 'failed', name: 'Failed' },
                { id: 'refunded', name: 'Refunded' },
            ]} />
            <SelectInput source="payment_method" choices={[
                { id: 'paypal', name: 'PayPal' },
                { id: 'zarinpal', name: 'ZarinPal' },
            ]} />
            <DateInput source="payment_date"/>
            <DateInput source="updated_at"/>
        </SimpleForm>
    </Edit>
);


export const PaymentCreate = () => (
    <Create>
        <SimpleForm>
        <NumberInput disabled source="id" />
            <ReferenceInput source="order" reference="orders" label="Order"/>
            <NumberInput source="amount" />
            <SelectInput source="status" choices={[
                { id: 'done', name: 'Done' },
                { id: 'failed', name: 'Failed' },
                { id: 'refunded', name: 'Refunded' },
            ]} />
            <SelectInput source="payment_method" choices={[
                { id: 'paypal', name: 'PayPal' },
                { id: 'zarinpal', name: 'ZarinPal' },
            ]} />
            <DateInput source="payment_date"/>
            <DateInput source="updated_at"/>
        </SimpleForm>
    </Create>
);