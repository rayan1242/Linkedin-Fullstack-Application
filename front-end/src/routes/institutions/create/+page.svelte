<script lang="ts">
    import { createInstitution, type InstitutionParam } from '$lib/api/institution'; // Adjust the import path as necessary
  
    let institution: InstitutionParam = {
      no_of_employees: 0,
      website: '',
      industry: '',
      name: '',
      description: '',
      location_city: '',
      location_state: '',
      location_country: ''
    };
  
    let message = '';
    let status = '';
  
    const handleSubmit = async () => {
      try {
        const response = await createInstitution(institution);
        if (response.status === 'success') {
          message = 'Institution created successfully!';
          handleRefresh();
        } else {
          message = `Error: ${response.message}`;
        }
      } catch (error) {
        console.error(error);
        message = 'Error creating institution.';
      }
    };
  
    const handleRefresh = () => {
      institution = {
        no_of_employees: 0,
        website: '',
        industry: '',
        name: '',
        description: '',
        location_city: '',
        location_state: '',
        location_country: ''
      };
      message = '';
    };
  </script>
  
  <form on:submit|preventDefault={handleSubmit}>
    <input type="number" bind:value={institution.no_of_employees} placeholder="Number of Employees" required />
    <input type="url" bind:value={institution.website} placeholder="Website" required />
    <input type="text" bind:value={institution.industry} placeholder="Industry" required />
    <input type="text" bind:value={institution.name} placeholder="Name" required />
    <input type="text" bind:value={institution.description} placeholder="Description" required />
    <input type="text" bind:value={institution.location_city} placeholder="City" required />
    <input type="text" bind:value={institution.location_state} placeholder="State" required />
    <input type="text" bind:value={institution.location_country} placeholder="Country" required />
    <button type="submit">Create Institution</button>
    <button on:click={handleRefresh}>Refresh</button>
  </form>
  
  
  {#if message}
    <p>{message}</p>
  {/if}
  <style>
    form {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      max-width: 400px;
      margin: 0 auto;
      padding: 2rem;
      border: 1px solid #ccc;
      border-radius: 8px;
      background-color: #f9f9f9;
    }

    input, button {
      padding: 0.5rem;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    input:focus {
      border-color: #007BFF;
      outline: none;
    }

    button {
      background-color: #007BFF;
      color: white;
      cursor: pointer;
    }

    button:hover {
      background-color: #0056b3;
    }

    p {
      text-align: center;
      color: green;
      font-weight: bold;
    }
  </style>