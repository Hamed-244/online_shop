import { List, Datagrid, TextField, EmailField, BooleanField, NumberField, RichTextField} from "react-admin";
import { Show, SimpleShowLayout, DateField} from 'react-admin';
import { Edit,EditButton, SimpleForm, TextInput, PasswordInput, DateInput,DateTimeInput, required, NumberInput, BooleanInput, ArrayInput, SimpleFormIterator } from 'react-admin';
import { Create , Filter, SearchInput,SelectInput, ReferenceInput,ReferenceField, ArrayField, ReferenceManyField,SingleFieldList,ChipField,ReferenceArrayInput,ReferenceArrayField} from 'react-admin';

const LogsFilter = [
    <SearchInput source="q" alwaysOn />,
    <ReferenceInput source="user" reference="users" label="Filter by user"/>,
    <TextInput source="action" label="Filter by Action"/>,
    <TextInput source="ip_address" label="Filter by Ip"/>
];
export const LogsList = () => (
    <List filters={LogsFilter}>
        <Datagrid rowClick="show">
            <NumberField source="id" />
            <ReferenceField source="user" reference="users" label="User"/>
            <TextField source="action" />
            <TextField source="ip_address" />
            <DateField source="timestamp"/>
        </Datagrid>
    </List>
);


export const LogShow = () => (
    <Show>
        <SimpleShowLayout>
            <NumberField source="id" />
            <ReferenceField source="user" reference="users" label="User"/>
            <TextField source="action" />
            <TextField source="ip_address" />
            <TextField source="details" fullWidth/>
            <DateField source="timestamp"/>
        </SimpleShowLayout>
    </Show>
);