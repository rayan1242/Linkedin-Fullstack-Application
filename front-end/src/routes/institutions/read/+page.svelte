<script lang="ts">
    import { getInstitution } from '$lib/api/institution'; // Adjust the import path as necessary
  
    let institution_id: string;
    let message = '';
    let institution: {
      institution_id?: number;
      no_of_employees?: number;
      website?: string;
      industry?: string;
      name?: string;
      description?: string;
      location_city?: string;
      location_state?: string;
      location_country?: string;
    } = {};
  
    const handleSubmit = async () => {
      try {
        const response = await getInstitution(institution_id);
        if (response.status === 'success') {
          institution = response.institution;
          message = '';
        } else {
          message = `Error: ${response.message}`;
          institution = {};
        }
      } catch (error) {
        console.error(error);
        message = 'Error fetching institution.';
        institution = {};
      }
    };
  </script>
  
  <form on:submit|preventDefault={handleSubmit}>
    <input type="number" bind:value={institution_id} placeholder="Institution ID" />
    <button type="submit">Get Institution</button>
  </form>
  
  {#if message}
    <p>{message}</p>
  {/if}
  
  {#if institution.institution_id}
    <div>
      <h2>Institution Details</h2>
      <p><strong>ID:</strong> {institution.institution_id}</p>
      <p><strong>Number of Employees:</strong> {institution.no_of_employees}</p>
      <p><strong>Website:</strong> {institution.website}</p>
      <p><strong>Industry:</strong> {institution.industry}</p>
      <p><strong>Name:</strong> {institution.name}</p>
      <p><strong>Description:</strong> {institution.description}</p>
      <p><strong>City:</strong> {institution.location_city}</p>
      <p><strong>State:</strong> {institution.location_state}</p>
      <p><strong>Country:</strong> {institution.location_country}</p>
    </div>
  {/if}

  <style>
    form {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      max-width: 400px;
      margin: 2rem auto;
      padding: 1rem;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f9f9f9;
    }
  
    input[type="number"] {
      padding: 0.5rem;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
  
    button {
      padding: 0.5rem 1rem;
      border: none;
      border-radius: 4px;
      background-color: #007bff;
      color: white;
      cursor: pointer;
    }
  
    button:hover {
      background-color: #0056b3;
    }
  
    p {
      color: red;
      text-align: center;
    }
  
    .institution-details {
      max-width: 600px;
      margin: 2rem auto;
      padding: 1rem;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f9f9f9;
    }
  
    .institution-details h2 {
      text-align: center;
      margin-bottom: 1rem;
    }
  
    .institution-details p {
      margin: 0.5rem 0;
    }
  
    .institution-details strong {
      display: inline-block;
      width: 150px;
    }
  </style>