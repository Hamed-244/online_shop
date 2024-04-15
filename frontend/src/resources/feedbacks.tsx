import { List, Datagrid, TextField, EmailField, BooleanField, NumberField, RichTextField} from "react-admin";
import { Show, SimpleShowLayout, DateField} from 'react-admin';
import { Edit,EditButton, SimpleForm, TextInput, PasswordInput, DateInput,DateTimeInput, required, NumberInput, BooleanInput, ArrayInput, SimpleFormIterator } from 'react-admin';
import { Create , Filter, SearchInput,SelectInput, ReferenceInput,ReferenceField, ArrayField, ReferenceManyField,SingleFieldList,ChipField,ReferenceArrayInput,ReferenceArrayField} from 'react-admin';

const FeedbackFilter = [
    <SearchInput source="q" alwaysOn />,
    <ReferenceInput source="order" reference="orders" label="Filter by Order" />,
    <NumberInput source="rating" label="Filter by rating" />,
];

export const FeedbackList = () => (
    <List filters={FeedbackFilter}>
        <Datagrid rowClick="show">
            <NumberField source="id" />
            <ReferenceField source="order" reference="orders" label="Order"/>
            <NumberField source="rating" />
            <DateField source="feedback_date"/>
            <DateField source="updated_at"/>
        </Datagrid>
    </List>
);


export const FeedbackShow = () => (
    <Show>
        <SimpleShowLayout>
            <NumberField source="id" />
            <ReferenceField source="order" reference="orders" label="Order"/>
            <NumberField source="rating" />
            <RichTextField aria-multiline source="comment" />
            <DateField source="feedback_date"/>
            <DateField source="updated_at"/>
        </SimpleShowLayout>
    </Show>
);


export const FeedbackEdit = () => (
    <Edit>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ReferenceInput source="order" reference="orders" label="Order"/>
            <NumberInput source="rating" />
            <TextInput multiline source="comment" fullWidth />
            <DateInput source="feedback_date"/>
            <DateInput source="updated_at"/>
        </SimpleForm>
    </Edit>
);


export const FeedbackCreate = () => (
    <Create>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ReferenceInput source="order" reference="orders" label="Order"/>
            <NumberInput source="rating" />
            <TextInput multiline source="comment" fullWidth />
        </SimpleForm>
    </Create>
);