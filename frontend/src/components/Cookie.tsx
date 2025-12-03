import React, { useState } from "react";
import "./Cookie.css";

interface Bite {
  cx: number;
  cy: number;
  r: number;
}

interface Crumb {
  id: number;
  cx: number;
  cy: number;
  r: number;
}

const maxSmallBites = 5;
const maxBites = 7; // 5 small bites + 1 large bite + 1 final bite

export default function Cookie() {
  const [bites, setBites] = useState<Bite[]>([]);
  const [crumbs, setCrumbs] = useState<Crumb[]>([]);

  const takeBite = () => {
    if (bites.length >= maxBites) return;

    if (bites.length < maxSmallBites) {
      // Small bites logic (first 5)
      const biteRadius = 25;
      const startAngle = -Math.PI / 4; // 45 degrees above horizontal to the right
      const endAngle = Math.PI / 4; // 45 degrees below horizontal to the right
      const angleStep = (endAngle - startAngle) / (maxSmallBites - 1);
      const radiusFromCenter = 90; // same as cookie radius

      const angle = startAngle + bites.length * angleStep;
      const cx = 100 + radiusFromCenter * Math.cos(angle);
      const cy = 100 + radiusFromCenter * Math.sin(angle);
      const r = biteRadius;

      const newBite: Bite = { cx, cy, r };
      setBites([...bites, newBite]);

      // Create multiple crumbs per bite
      const newCrumbs: Crumb[] = Array.from({ length: 5 }).map((_, i) => ({
        id: crumbs.length + i,
        cx: cx + (Math.random() * 20 - 10),
        cy: cy + (Math.random() * 10),
        r: Math.random() * 4 + 2,
      }));
      setCrumbs([...crumbs, ...newCrumbs]);
    } else if (bites.length === maxSmallBites) {
      // Large bite removing ~75% of cookie, leaving a small piece
      // We'll position the large bite center from the same direction as the small bites (top-right edge)
      // Position the large bite center slightly off center towards top-right
      // The previous small bites are around 45 degrees, so place large bite center accordingly

      const angle = 0; // 0 radians (to the right)
      const radiusFromCenter = 100; // slightly outside the cookie center
      const cx = 100 + radiusFromCenter * Math.cos(angle);
      const cy = 100 + radiusFromCenter * Math.sin(angle) + 20; // shift down a bit to cover cookie better
      const r = 90; // radius covers most of the cookie

      const newBite: Bite = { cx, cy, r };
      setBites([...bites, newBite]);

      // Create crumbs for large bite (more crumbs)
      const newCrumbs: Crumb[] = Array.from({ length: 20 }).map((_, i) => ({
        id: crumbs.length + i,
        cx: cx + (Math.random() * 60 - 30),
        cy: cy + (Math.random() * 40 - 20),
        r: Math.random() * 6 + 3,
      }));
      setCrumbs([...crumbs, ...newCrumbs]);
    } else if (bites.length === maxSmallBites + 1) {
      // Final bite removes the rest of the cookie
      // Represent final bite as a circle covering the remaining small piece
      const cx = 100;
      const cy = 60;
      const r = 50;

      const newBite: Bite = { cx, cy, r };
      setBites([...bites, newBite]);

      // Create crumbs for final bite
      const newCrumbs: Crumb[] = Array.from({ length: 10 }).map((_, i) => ({
        id: crumbs.length + i,
        cx: cx + (Math.random() * 30 - 15),
        cy: cy + (Math.random() * 20 - 10),
        r: Math.random() * 5 + 2,
      }));
      setCrumbs([...crumbs, ...newCrumbs]);
    }
  };

  const resetCookie = () => {
    setBites([]);
    setCrumbs([]);
  };

  // Hide cookie after final bite
  const showCookie = bites.length < maxBites;

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      {showCookie && (
        <svg
          width="200"
          height="200"
          viewBox="0 0 200 200"
          onClick={takeBite}
          style={{ cursor: "pointer" }}
        >
          <defs>
            <mask id="biteMask">
              <rect width="200" height="200" fill="white" />
              {bites.map((bite, i) => {
                if (i < maxSmallBites) {
                  // Small bites with teeth effect
                  return (
                    <g key={i}>
                      <circle cx={bite.cx} cy={bite.cy} r={bite.r} fill="black" />
                      <circle
                        cx={bite.cx + bite.r / 2}
                        cy={bite.cy - bite.r / 2}
                        r={bite.r / 3}
                        fill="black"
                      />
                      <circle
                        cx={bite.cx - bite.r / 2}
                        cy={bite.cy + bite.r / 2}
                        r={bite.r / 3}
                        fill="black"
                      />
                      <circle
                        cx={bite.cx + bite.r / 3}
                        cy={bite.cy + bite.r / 3}
                        r={bite.r / 4}
                        fill="black"
                      />
                      <circle
                        cx={bite.cx - bite.r / 3}
                        cy={bite.cy - bite.r / 3}
                        r={bite.r / 4}
                        fill="black"
                      />
                      <circle
                        cx={bite.cx + bite.r / 1.5}
                        cy={bite.cy}
                        r={bite.r / 5}
                        fill="black"
                      />
                      <circle
                        cx={bite.cx - bite.r / 1.5}
                        cy={bite.cy}
                        r={bite.r / 5}
                        fill="black"
                      />
                      <circle
                        cx={bite.cx}
                        cy={bite.cy + bite.r / 1.5}
                        r={bite.r / 5}
                        fill="black"
                      />
                      <circle
                        cx={bite.cx}
                        cy={bite.cy - bite.r / 1.5}
                        r={bite.r / 5}
                        fill="black"
                      />
                    </g>
                  );
                } else {
                  // Large bites: just a single large circle
                  return <circle key={i} cx={bite.cx} cy={bite.cy} r={bite.r} fill="black" />;
                }
              })}
            </mask>
          </defs>

          {/* Cookie base */}
          <circle cx="100" cy="100" r="90" fill="#D2691E" mask="url(#biteMask)" />

          {/* Chocolate chips */}
          {/* Hide chips within large bite by applying the same mask */}
          <circle cx="70" cy="80" r="10" fill="#4B2E2E" mask="url(#biteMask)" />
          <circle cx="130" cy="60" r="8" fill="#4B2E2E" mask="url(#biteMask)" />
          <circle cx="120" cy="140" r="7" fill="#4B2E2E" mask="url(#biteMask)" />
          <circle cx="80" cy="130" r="6" fill="#4B2E2E" mask="url(#biteMask)" />
          <circle cx="90" cy="110" r="8" fill="#4B2E2E" mask="url(#biteMask)" />
          <circle cx="110" cy="90" r="6" fill="#4B2E2E" mask="url(#biteMask)" />
          <circle cx="140" cy="100" r="7" fill="#4B2E2E" mask="url(#biteMask)" />
          <circle cx="60" cy="120" r="5" fill="#4B2E2E" mask="url(#biteMask)" />

          {/* Crumbs */}
          {crumbs.map((crumb) => (
            <circle
              key={crumb.id}
              className="crumb"
              cx={crumb.cx}
              cy={crumb.cy}
              r={crumb.r}
              fill="#D2A679"
            />
          ))}
        </svg>
      )}

      {bites.length >= maxBites && (
        <div style={{ marginTop: "20px" }}>
          <p>Cookie finished! 🍪</p>
          <button onClick={resetCookie}>Reset</button>
        </div>
      )}
    </div>
  );
}