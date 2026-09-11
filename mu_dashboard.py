import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(
    page_title="Marwadi University 3D & Campus Hub",
    page_icon="🏛️",
    layout="wide"
)

# 2. Sidebar Navigation
st.sidebar.title("MU Campus Navigation")
option = st.sidebar.selectbox(
    "Choose View",
    ["Dashboard Overview", "Interactive 3D View", "360° Virtual Tour Link", "Campus Infrastructure Blocks"]
)

# 3. Main Title & Description
st.title("🏛️ Marwadi University - Interactive 3D & Campus Portal")
st.markdown("Explore the 52-acre Marwadi University campus infrastructure, facilities, and virtual spaces interactively.")

# --- OPTION 1: DASHBOARD OVERVIEW ---
if option == "Dashboard Overview":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Campus Area", "52 Acres", "Vast Green Space")
    col2.metric("Academic Blocks", "3 Main Blocks", "Engineering, PG, Law/Management")
    col3.metric("Students", "10,000+", "Global & Domestic")
    col4.metric("CCTV Security", "1,700 Cameras", "24/7 Live Tracking")

    st.markdown("---")
    st.subheader("About the Campus Layout")
    st.write("""
    Marwadi University features state-of-the-art infrastructure located on Morbi Road, Rajkot. 
    The campus includes modern academic zones, an extensive Learning Resource Center, 
    an auditorium, a large amphitheatre, and student residences.
    """)

# --- OPTION 2: INTERACTIVE 3D VIEW (UPGRADED FOR CLARITY) ---
elif option == "Interactive 3D View":
    st.subheader("Interactive 3D Campus Block & Building Map")
    st.markdown("This enhanced 3D view maps out key campus zones with **clear visual labels and color coding**. Click and drag your mouse to rotate and inspect.")

    # Enhanced Three.js HTML/JS 3D Scene with Clear Labels
    three_js_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; background-color: #0e1117; color: white; font-family: sans-serif; overflow: hidden; }
            #canvas-container { width: 100%; height: 500px; display: block; position: relative; }
            .building-label {
                position: absolute;
                background: rgba(0, 0, 0, 0.85);
                color: #ffffff;
                padding: 4px 8px;
                font-size: 11px;
                font-weight: bold;
                border-radius: 4px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                pointer-events: none;
                transform: translate(-50%, -100%);
                white-space: nowrap;
                display: none;
            }
            #instructions {
                position: absolute;
                top: 10px;
                left: 10px;
                background: rgba(15, 23, 42, 0.9);
                padding: 10px 14px;
                border-radius: 6px;
                font-size: 13px;
                border-left: 4px solid #ff4b4b;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            }
        </style>
    </head>
    <body>
        <div id="instructions">
            <b>Controls:</b> Click & Drag to Rotate | Scroll to Zoom<br>
            <span style="color: #94a3b8; font-size: 11px;">Labels track the 3D structures dynamically</span>
        </div>
        
        <div id="canvas-container">
            <!-- HTML Overlay Labels for Clarity -->
            <div id="label-main" class="building-label">Main Building (Engineering)</div>
            <div id="label-pg" class="building-label">PG & Admin Block</div>
            <div id="label-law" class="building-label">Law & Management</div>
            <div id="label-auditorium" class="building-label">Auditorium & Events</div>
        </div>

        <!-- Include Three.js via CDN -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script>
            const container = document.getElementById('canvas-container');
            const scene = new THREE.Scene();
            scene.background = new THREE.Color(0x0e1117);

            const camera = new THREE.PerspectiveCamera(50, container.clientWidth / container.clientHeight, 0.1, 1000);
            camera.position.set(0, 16, 26);

            const renderer = new THREE.WebGLRenderer({ antialias: true });
            renderer.setSize(container.clientWidth, container.clientHeight);
            container.appendChild(renderer.domElement);

            // Lighting
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.8);
            scene.add(ambientLight);

            const dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
            dirLight.position.set(15, 30, 20);
            scene.add(dirLight);

            // Campus Group Container
            const campusGroup = new THREE.Group();

            // 1. Main Building (Blue)
            const geoMain = new THREE.BoxGeometry(6, 4, 3.5);
            const matMain = new THREE.MeshStandardMaterial({ color: 0x2e86de, roughness: 0.3 });
            const mainMesh = new THREE.Mesh(geoMain, matMain);
            mainMesh.position.set(-6, 2, 0);
            mainMesh.userData = { labelId: 'label-main', vector: new THREE.Vector3(-6, 4.5, 0) };
            campusGroup.add(mainMesh);

            // 2. PG Building (Green)
            const geoPG = new THREE.BoxGeometry(4.5, 5, 3);
            const matPG = new THREE.MeshStandardMaterial({ color: 0x10ac84, roughness: 0.3 });
            const pgMesh = new THREE.Mesh(geoPG, matPG);
            pgMesh.position.set(1.5, 2.5, -3);
            pgMesh.userData = { labelId: 'label-pg', vector: new THREE.Vector3(1.5, 5.5, -3) };
            campusGroup.add(pgMesh);

            // 3. Law & Management Block (Orange)
            const geoLaw = new THREE.BoxGeometry(4, 3.5, 4);
            const matLaw = new THREE.MeshStandardMaterial({ color: 0xff9f43, roughness: 0.3 });
            const lawMesh = new THREE.Mesh(geoLaw, matLaw);
            lawMesh.position.set(5.5, 1.75, 2.5);
            lawMesh.userData = { labelId: 'label-law', vector: new THREE.Vector3(5.5, 4, 2.5) };
            campusGroup.add(lawMesh);

            // 4. Auditorium Block (Purple)
            const geoAud = new THREE.CylinderGeometry(2.5, 2.5, 3, 32);
            const matAud = new THREE.MeshStandardMaterial({ color: 0x9b59b6, roughness: 0.3 });
            const audMesh = new THREE.Mesh(geoAud, matAud);
            audMesh.position.set(-1.5, 1.5, 4);
            audMesh.userData = { labelId: 'label-auditorium', vector: new THREE.Vector3(-1.5, 3.5, 4) };
            campusGroup.add(audMesh);

            // Ground plane (Campus Floor)
            const groundGeo = new THREE.PlaneGeometry(35, 35);
            const groundMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.9 });
            const ground = new THREE.Mesh(groundGeo, groundMat);
            ground.rotation.x = -Math.PI / 2;
            scene.add(ground);

            scene.add(campusGroup);

            // Mouse Interaction Logic
            let isDragging = false;
            let previousMousePosition = { x: 0, y: 0 };

            container.addEventListener('mousedown', (e) => { isDragging = true; });
            window.addEventListener('mouseup', (e) => { isDragging = false; });
            container.addEventListener('mousemove', (e) => {
                if (isDragging) {
                    const deltaX = e.clientX - previousMousePosition.x;
                    const deltaY = e.clientY - previousMousePosition.y;
                    campusGroup.rotation.y += deltaX * 0.008;
                    campusGroup.rotation.x += deltaY * 0.008;
                }
                previousMousePosition = { x: e.clientX, y: e.clientY };
            });

            // Update HTML Label positions dynamically based on 3D coordinates
            const meshes = [mainMesh, pgMesh, lawMesh, audMesh];
            function updateLabels() {
                meshes.forEach(mesh => {
                    const label = document.getElementById(mesh.userData.labelId);
                    const v = mesh.userData.vector.clone();
                    v.applyMatrix4(campusGroup.matrixWorld);
                    v.project(camera);

                    const x = (v.x *  .5 + .5) * container.clientWidth;
                    const y = (v.y * -.5 + .5) * container.clientHeight;

                    if (v.z < 1) {
                        label.style.display = 'block';
                        label.style.left = `${x}px`;
                        label.style.top = `${y}px`;
                    } else {
                        label.style.display = 'none';
                    }
                });
            }

            // Animation Loop
            function animate() {
                requestAnimationFrame(animate);
                if (!isDragging) {
                    campusGroup.rotation.y += 0.002;
                }
                renderer.render(scene, camera);
                updateLabels();
            }
            animate();

            window.addEventListener('resize', () => {
                camera.aspect = container.clientWidth / container.clientHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(container.clientWidth, container.clientHeight);
            });
        </script>
    </body>
    </html>
    """
    
    st.components.v1.html(three_js_code, height=530)
    
    # Legend guide underneath for crystal clear clarity
    st.markdown("### 🗺️ Campus Zone Legend")
    col_l1, col_l2, col_l3, col_l4 = st.columns(4)
    col_l1.markdown("🔵 **Main Building** (Engineering)")
    col_l2.markdown("🟢 **PG & Admin Block**")
    col_l3.markdown("🟠 **Law & Management**")
    col_l4.markdown("🟣 **Auditorium** (Events)")

# --- OPTION 3: 360 VIRTUAL TOUR LINK ---
elif option == "360° Virtual Tour Link":
    st.subheader("Immersive Campus Walkthrough")
    st.write("Access the official 360-degree panoramic tour views via a clean external link:")
    st.markdown(
        '<a href="https://marwadiuniversity.ac.in/360-virtual-tour/" target="_blank">'
        '<button style="background-color: #ff4b4b; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">'
        '🌐 Open Official Marwadi University 360° Tour in New Tab</button></a>',
        unsafe_allow_html=True
    )

# --- OPTION 4: CAMPUS INFRASTRUCTURE BLOCKS ---
elif option == "Campus Infrastructure Blocks":
    st.subheader("Key Building Directory")
    data = {
        "Building Name": ["Main Building", "PG Building", "Law & Management Block", "Auditorium & Amphitheatre", "Hostels & Mess"],
        "Primary Function": ["Engineering classes, mini canteens, stationery", "Administrative offices, seminar halls", "Law, Commerce, and Management departments", "Cultural events, large gatherings (800+ capacity)", "Student residential zone & dining"],
        "Status": ["Active", "Active", "Active", "Active", "Active"]
    }
    df = pd.DataFrame(data)
    st.table(df)
