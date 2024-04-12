import { List, Datagrid, TextField, EmailField, BooleanField, NumberField, SearchInput, ReferenceField,ReferenceInput} from "react-admin";
import { Show, SimpleShowLayout, DateField,ImageField,ImageInput} from 'react-admin';
import { Edit, SimpleForm, TextInput, PasswordInput,DateTimeInput, required, NumberInput, BooleanInput, ArrayInput, SimpleFormIterator } from 'react-admin';
import { Create , Filter} from 'react-admin';

const ProductImageFilter = [
    <SearchInput source="q" alwaysOn />,
    <NumberInput label="Filter by Product" source="product" />,

];

export const ProductImageList = () => (
    <List filters={ProductImageFilter}>
        <Datagrid rowClick="show">
            <NumberField source="id" />
            <ImageField source="image"  sx={{ '& img': { maxWidth: 40, maxHeight: 40, objectFit: 'contain' } }}/>
            <ReferenceField source="product" reference="products" label="Product"/>
            <DateField source="created_at" />
        </Datagrid>
    </List>
);

export const ProductImageShow = () => (
    <Show >
        <SimpleShowLayout>
            <ImageField source="image"  sx={{ '& img': { maxWidth: 1000, objectFit: 'contain' } }}/>
            <NumberField source="id" />
            <ReferenceField source="product" reference="products" label="Product"/>
            <DateField source="created_at" />
        </SimpleShowLayout>
    </Show>
);

export const ProductImageEdit = () => (
    <Edit>
        <SimpleForm>
            <NumberInput disabled source="id" />
            <ImageField source="image" title="Last Image" />
            <ImageInput source="image" minSize={5000} placeholder="Drop a picture to upload, or click to select it and update last picture">
                <ImageField source="src" title="New Image" />
            </ImageInput>
            <ReferenceInput title="Product" source="product" reference="products">
            </ReferenceInput>
            <DateTimeInput source="created_at" />
        </SimpleForm>
    </Edit>
);

export const ProductImageCreate = () => (
    <Create >
        <SimpleForm>
            <ImageField source="image" title="Last Image" />
            <ImageInput source="image" minSize={5000}>
                <ImageField source="src" title="title" />
            </ImageInput>
            <ReferenceInput title="Product" source="product" reference="products">
            </ReferenceInput>
        </SimpleForm>
    </Create>
);
