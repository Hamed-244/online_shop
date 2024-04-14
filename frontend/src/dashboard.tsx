import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import * as React from "react";
import { Title } from 'react-admin';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

interface DashboardInfo {
    payment: Record<string, number>;
    popular: Record<string, number>;
    "weekly-sales": number; // Update property name
    "weekly-payments": number; // Update property name
    "total-revenue": number; // Update property name
}

const Dashboard = () => {
    const [dashboardInfo, setDashboardInfo] = React.useState<DashboardInfo | null>(null);

    React.useEffect(() => {
        const fetchData = async () => {
            // Get the token from localStorage
            const token = localStorage.getItem('access');
        
            // Prepare the headers with Authorization
            const headers = {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json' // Adjust content type as needed
            };
        
            // Make the fetch request with headers
            try {
                const response = await fetch(import.meta.env.VITE_REST_URL + '/dashboard-info', {
                    method: 'GET',
                    headers: headers
                });
        
                // Handle response
                if (response.ok) {
                    const data = await response.json();
                    setDashboardInfo(data);
                } else {
                    // Handle error
                    console.error('Failed to fetch dashboard info:', response.statusText);
                }
            } catch (error) {
                console.error('Error fetching dashboard info:', error);
            }
        };

        fetchData();
    }, []);

    if (!dashboardInfo) return null;

    // Prepare data for line chart (payments for last 7 days)
    const paymentData = Object.entries(dashboardInfo.payment)
        .slice(-7) // Get the last 7 entries
        .map(([date, sales]) => ({ date, sales }));

    const popularData = Object.entries(dashboardInfo.popular).map(([product, sales]) => ({
        product,
        sales
    }));

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
            <Typography variant="h3" sx={{marginBottom:8,marginTop:5}} gutterBottom>Welcome to Admin Panel</Typography>

            <Card style={{ width: '100%', marginBottom: '20px', padding: '20px'}}>
                    <Typography variant="h6">Weekly Sales: {dashboardInfo["weekly-sales"]}</Typography>
                    <Typography variant="h6">Weekly Payments: {dashboardInfo["weekly-payments"]}</Typography>
                    <Typography variant="h6">Total Revenue: {dashboardInfo["total-revenue"]}</Typography>
            </Card>

            <div style={{width:'100%', display: 'flex', flexDirection: 'row', flexWrap:'wrap', alignItems: 'stretch' , justifyContent:'space-between'}}>
                <Card style={{ width: '45%', marginBottom: '20px', padding: '20px'}}>
                    <Typography variant="h5" marginBottom={2}>Payments for Last 7 Days</Typography>

                    <LineChart width={700} height={300} data={paymentData}>
                        <XAxis dataKey="date" />
                        <YAxis />
                        <CartesianGrid stroke="#eee" strokeDasharray="5 5" />
                        <Line dataKey="sales" type="monotone" stroke="rgb(0 156 241)" />
                        <Tooltip />
                    </LineChart>
                </Card>

                <Card style={{ width: '45%', marginBottom: '20px', padding: '20px'}}>
                    <Typography variant="h5" marginBottom={2}>Most Popular Products</Typography>
                    <BarChart width={700} height={300} data={popularData}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="product" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="sales" barSize={30} fill="rgb(0 156 241)" />
                    </BarChart>
                </Card>
            </div>
        </div>
    );
};

export default Dashboard;
