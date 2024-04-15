import { List, Datagrid, TextField, EmailField, BooleanField, NumberField, RichTextField,ImageField,ImageInput} from "react-admin";
import { Show, SimpleShowLayout, DateField} from 'react-admin';
import { Edit,EditButton, SimpleForm, TextInput, PasswordInput, DateInput,DateTimeInput, required, NumberInput, BooleanInput, ArrayInput, SimpleFormIterator } from 'react-admin';
import { Create , Filter, SearchInput,SelectInput, ReferenceInput,ReferenceField, ArrayField, ReferenceManyField,SingleFieldList,ChipField,ReferenceArrayInput,ReferenceArrayField} from 'react-admin';

const ProductsFilter = [
    <SearchInput source="q" alwaysOn />,
    <TextInput label="Filter by Name" source="name" />,
    <TextInput label="Filter by Slug" source="slug" />,
    <NumberInput label="Filter by Price" source="price" />,
    <ReferenceArrayInput source="category" reference="categories" label="Filter by Category" />
];


export const ProductsList = () => (
    <List filters={ProductsFilter}>
        <Datagrid rowClick="show">
            <NumberField source="id" />
            <ImageField source="image" title="Last Image" sx={{ '& img': { maxWidth: 40, maxHeight: 40, objectFit: 'contain' } }}/>
            <TextField source="name" />
            <TextField source="slug" />
            <TextField aria-multiline source="description" />
            <NumberField source="price" />
            <NumberField source="amount" />

            <ReferenceArrayField source="category" reference="categories" label="Categories"/>
        </Datagrid>
    </List>
);


export const ProductShow = () => (
    <Show>
        <SimpleShowLayout>
            <NumberField source="id" />
            <ImageField source="image" title="Last Image" />
            <TextField source="name" />
            <TextField source="slug" />
            <TextField aria-multiline source="description" />
            <NumberField source="price" />
            <NumberField source="amount" />
            <ReferenceArrayField source="category" reference="categories" label="Categories"/>
        </SimpleShowLayout>
    </Show>
);


export const ProductEdit = () => (
    <Edit>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ImageField source="image" title="Last Image" />
            <ImageInput source="image" minSize={5000} placeholder="Drop a picture to upload, or click to select it and update last picture">
                <ImageField source="src" title="New Image" />
            </ImageInput>
            <TextInput source="name" />
            <TextInput source="slug" />
            <TextInput aria-multiline source="description" />
            <NumberInput source="price" />
            <NumberInput source="amount" />
            <ReferenceArrayInput source="category" reference="categories" label="Categories"/>
        </SimpleForm>
    </Edit>
);


export const ProductCreate = () => (
    <Create>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ImageField source="image" title="Last Image" />
            <ImageInput source="image" minSize={5000} placeholder="Drop a picture to upload, or click to select it and update last picture">
                <ImageField source="src" title="New Image" />
            </ImageInput>
            <TextInput source="name" />
            <TextInput source="slug" />
            <TextInput aria-multiline source="description" />
            <NumberInput source="price" />
            <NumberInput source="amount" />
            <ReferenceArrayInput source="category" reference="categories" label="Categories"/>
        </SimpleForm>
    </Create>
);