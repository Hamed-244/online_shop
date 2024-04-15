import { List, Datagrid, TextField, EmailField, BooleanField, NumberField, RichTextField} from "react-admin";
import { Show, SimpleShowLayout, DateField} from 'react-admin';
import { Edit,EditButton, SimpleForm, TextInput, PasswordInput, DateInput,DateTimeInput, required, NumberInput, BooleanInput, ArrayInput, SimpleFormIterator } from 'react-admin';
import { Create , Filter, SearchInput,SelectInput, ReferenceInput,ReferenceField, ArrayField, ReferenceManyField,SingleFieldList,ChipField,ReferenceArrayInput,ReferenceArrayField} from 'react-admin';

const NoticesFilter = [
    <SearchInput source="q" alwaysOn />,
    <ReferenceInput source="user" reference="users" label="Filter by User" />,
    <SelectInput source="type" label="Filter by type" choices={[
        { id: 'danger', name: 'Danger' },
        { id: 'success', name: 'Success' },
        { id: 'warn', name: 'Warn' },
    ]} />
];

export const NoticeList = () => (
    <List filters={NoticesFilter}>
        <Datagrid rowClick="show">
            <NumberField source="id" />
            <ReferenceField source="user" reference="users" label="User"/>
            <TextField source="type"/>
            <TextField source="title"/>
            <DateField source="created_at"/>
        </Datagrid>
    </List>
);


export const NoticeShow = () => (
    <Show>
        <SimpleShowLayout>
            <NumberField source="id" />
            <ReferenceField source="user" reference="users" label="User"/>
            <TextField source="type"/>
            <TextField source="title"/>
            <TextField source="message" />
            <DateField source="created_at"/>
        </SimpleShowLayout>
    </Show>
);


export const NoticeEdit = () => (
    <Edit>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ReferenceInput source="user" reference="users" label="User"/>
            <SelectInput source="type" choices={[
                { id: 'danger', name: 'Danger' },
                { id: 'success', name: 'Success' },
                { id: 'warn', name: 'Warn' },
            ]} />
            <TextInput source="title"/>
            <TextInput source="message" fullWidth/>
            <DateInput source="created_at"/>
        </SimpleForm>
    </Edit>
);


export const NoticeCreate = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="user" reference="users" label="User"/>
            <SelectInput source="type" choices={[
                { id: 'danger', name: 'Danger' },
                { id: 'success', name: 'Success' },
                { id: 'warn', name: 'Warn' },
            ]} />
            <TextInput source="title"/>
            <TextInput source="message" fullWidth/>
        </SimpleForm>
    </Create>
);