<div style="display: flex; justify-content: center">
  <img src="https://github.com/user-attachments/assets/7e6106c2-eeef-4ce7-a9ff-707f6499c704" width="200" height="150" style="margin-right: 20px">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/a8d1c34a-f5c1-4ab9-99c3-0d965ab5a676" width="310" height="124">
</div>

<h1>
  Dispa - SET UNLEASH
  <br>
  Data Framework and EWH/HPWH-based VPP Integration for Belgian Flexibility Assessment
</h1>

Ray Rojas<sup>1,2</sup>, David Rojas<sup>1</sup>, Marco Navia<sup>1</sup>, Julio Pascual<sup>2</sup>, Sylvain Quoilin<sup>1</sup>
<br>
> <sup>1</sup>University of Liège, Department of Aerospace and Mechanical Engineering, Sart Tilman, Liège, Belgium
> <br>
> <sup>2</sup>Public University of Navarre, Department of Electrical, Electronic and Communication Engineering, Pamplona, Spain

### Overview 

This repository accompanies the UNLEASH project deliverables (D5.1 and D5.2), providing:
- Automated data pipelines for the Dispa-SET Unit Commitment and Economic Dispatch (UCED) model, covering 30 European countries (2016–2023) at hourly/30-min/15-min resolution.
- Virtual Power Plant (VPP) modeling of 500,000 residential water heaters (1245 MW capacity, 7543 MWh storage) as a Boundary Sector in Dispa-SET.

### Key Features  
- **Open-Source Data Framework**  
  - Standardized data processing for Dispa-SET via Python/API automation (ENTSO-E, web scraping).  
  - Covers techno-economic (e.g., plant efficiencies, costs) and dynamic (e.g., hourly demand, VRES generation) inputs.  
- **VPP as Boundary Sector**  
  - Models aggregated water heaters as a P2X technology with thermal storage constraints.  
  - Includes SOC dynamics and demand profiles.
 
### Getting Started
